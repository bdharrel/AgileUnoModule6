"""
Bridget D. Harrell
Module 6
bdharrel@uno.edu
"""

import sys
import json

with open ("input.json", "r") as input:
    customers = json.load(input)


#are all customer numbers unique?
temp = []
for value in customers ["clients"]:
    temp.append(value["id"])

#add values to set
unique = set(temp)
#add values to tuple
original = (temp)

if len(unique) != len(original):
    print("There are duplicate id mumbers in the data, exiting!!!")
    sys.exit
else:
    print("All customer ids are unique!!!")
