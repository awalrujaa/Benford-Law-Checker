# Benford-Law-Checker
Benford Law Checker

Overview
Benford’s law describes the relative frequency distribution for leading digits of numbers in datasets. 
Leading digits with smaller values occur more frequently than larger values. 
This law states that approximately 30% of numbers start with a 1 while less than 5% start with a 9. 
According to this law, leading 1s appear 6.5 times as often as leading 9s! Benford’s law is also known as the First Digit Law.

If leading digits 1 – 9 had an equal probability, they’d each occur 11.1% of the time. However, that is not true in many datasets. 
The graph displays the distribution of leading digits according to Benford’s law.

How to Use
Install the dependencies:
pip install pyramid

Create or download a csv file of 10k+ numbers.
Run python app.py.

Open index.html and upload the csv.

Check the result is given in json format.
