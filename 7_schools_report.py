"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""

import json

infile = open("school_data.json", "r")
school_data = json.load(infile)
infile.close()

print("Schools with Women Graduation Rate Over 75")
print("------------------------------------------")

for school in school_data:
    school_name = school["instnm"]
    grad_rate = school["Graduation rate  women (DRVGR2020)"]

    if grad_rate != None:
        if grad_rate > 75:
            print(school_name)
            print("Women Graduation Rate:", grad_rate)
            print()

print()
print("Schools with Off Campus Price Over $60,000")
print("------------------------------------------")

for school in school_data:
    school_name = school["instnm"]
    price = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]

    if price != None:
        if price > 60000:
            print(school_name)
            print("Off Campus Price:", price)
            print()
