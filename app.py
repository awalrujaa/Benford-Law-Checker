import csv
import math
import json
from pyramid.config import Configurator
from pyramid.response import Response

def benfords_law(num_list):
    """
    Checks if the given list of numbers follows Benford's Law.
    Returns True if the list follows Benford's Law, False otherwise.
    """
    first_digits = [int(str(num)[0]) for num in num_list]
    digit_counts = [first_digits.count(digit) for digit in range(1, 10)]
    digit_frequencies = [count / len(num_list) for count in digit_counts]
    benford_frequencies = [math.log10(1 + 1/digit) for digit in range(1, 10)]
    return all(abs(benford_frequencies[i] - digit_frequencies[i]) < 0.02 for i in range(9))

def check_benford_csv(file_path):
    """
    Reads a CSV file and checks if the first column of numbers follows Benford's Law.
    Returns True if the first column follows Benford's Law, False otherwise.
    """
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        num_list = [int(row[0]) for row in reader if row and row[0].isdigit()]
    return benfords_law(num_list)

def benford_view(request):
    """
    Pyramid view function for the /benford endpoint.
    Reads the uploaded CSV file, checks if the first column follows Benford's Law,
    and returns a JSON response with the result.
    """
    if 'csvfile' not in request.POST:
        return Response(json.dumps({"error": "No CSV file provided."}), status=400)
    
    csvfile = request.POST['csvfile'].file
    csvreader = csv.reader(csvfile)
    num_list = [int(row[0]) for row in csvreader if row and row[0].isdigit()]
    
    if len(num_list) < 10000:
        return Response(json.dumps({"error": "CSV file must have 10k+ rows."}), status=400)
    
    if benfords_law(num_list):
        return Response(json.dumps({"result": "CSV file conforms to Benford's Law."}), content_type="application/json")
    else:
        return Response(json.dumps({"result": "CSV file does not conform to Benford's Law."}), content_type="application/json")

if __name__ == '__main__':
    config = Configurator()
    config.add_route('benford', '/benford')
    config.add_view(benford_view, route_name='benford', renderer='json')
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=8080)
