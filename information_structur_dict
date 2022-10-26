#! /usr/bin/env python3

import re
import sys

if len(sys.argv) == 1:
    print("No filename was given")
    try:
        infile = open(input("Please enter the filename: "), "r")
    except IOError as err:
        print("Could not load file due to: ",str(err))
        sys.exit(1)

# If filename is given, open file
if len(sys.argv) == 2:
    try:
        infile = open(sys.argv[1], "r")
    except IOError as err:
        print("Could not load file due to: ",str(err))
        sys.exit(1)


first_name_dict = dict()
last_name_dict = dict()
height_dict = dict()
weight_dict = dict()
eye_color_dict = dict()
blood_type_dict = dict()
children_dict = dict()
first_line_read = False
CPR = ""

for line in infile:
    if line[0] == "#":
        continue

    if line[:3] == "CPR" and first_line_read and CPR not in children_dict:
        children_dict[CPR] = "None"

    if line[:3] == "CPR":
        cpr_search = re.search(r'(\d{6}\-\d{4})', line)
        CPR = cpr_search.group(1)
        first_line_read = True

    if line[0:10] == "First name":
        first_name_dict[CPR] = line[12:-1]

    if line[:9] == "Last name":
        last_name_dict[CPR] = line[11:-1]

    if line[:6] == "Height":
        height_dict[CPR] = line[8:-1]

    if line[:6] == "Weight":
        weight_dict[CPR] = line[8:-1]

    if line[:9] == "Eye color":
        eye_color_dict[CPR] = line[11:-1]

    if line[:10] == "Blood type":
        blood_type_dict[CPR] = line[12:-1]

    if line[:8] == "Children":
        children_dict[CPR] = re.findall(r'\d{6}\-\d{4}', line)

if CPR not in children_dict:
    children_dict[CPR] = "None"

print(len(first_name_dict))
print(len(last_name_dict))
print(len(height_dict))
print(len(weight_dict))
print(len(eye_color_dict))
print(len(blood_type_dict))
print(len(children_dict),"\n")

print(first_name_dict["230226-9781"])
print(last_name_dict["230226-9781"])
print(height_dict["230226-9781"])
print(weight_dict["230226-9781"])
print(eye_color_dict["230226-9781"])
print(blood_type_dict["230226-9781"])
print(children_dict["230226-9781"],"\n")

print(first_name_dict["120194-9148"])
print(last_name_dict["120194-9148"])
print(height_dict["120194-9148"])
print(weight_dict["120194-9148"])
print(eye_color_dict["120194-9148"])
print(blood_type_dict["120194-9148"])
print(children_dict["120194-9148"])