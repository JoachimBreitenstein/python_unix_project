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

# People_dict is a dictionary with a person's CPR as key and the value is a list of:
# [First name, Last name, Height, Weight, Eye colour, Blood type, Children, Mother, Father, grand parents]
people_dict = {}

for line in infile:

    if line[:3] == "CPR":
        cpr_search = re.search(r'(\d{6}\-\d{4})', line)
        CPR = cpr_search.group(1)
        if CPR not in people_dict.keys():
            people_dict[CPR] = [None, None, None, None, None, None, None, None, None]


    if line[0:10] == "First name":
        people_dict[CPR][0] = line[12:-1]

    if line[:9] == "Last name":
        people_dict[CPR][1] = line[11:-1]

    if line[:6] == "Height":
        people_dict[CPR][2] = line[8:-1]

    if line[:6] == "Weight":
        people_dict[CPR][3] = line[8:-1]

    if line[:9] == "Eye color":
        people_dict[CPR][4] = line[11:-1]

    if line[:10] == "Blood type":
        people_dict[CPR][5] = line[12:-1]

    if line[:8] == "Children":
        people_dict[CPR][6] = re.findall(r'\d{6}\-\d{4}', line)
        for i in range(len(people_dict[CPR[6]])):

            if people_dict[CPR][6][i] in people_dict.keys():
                if CPR[-1] in ("2","4","6","8"):
                    people_dict[people_dict[CPR][6][i]][7] = CPR
                if CPR[-1] in ("1","3","5","7","9"):
                    people_dict[people_dict[CPR][6][i]][8] = CPR

            else:
                if CPR[-1] in ("2","4","6","8"):
                    people_dict[people_dict[CPR][6][i]] = [None, None, None, None, None, None, None, CPR, None]
                if CPR[-1] in ("1","3","5","7","9"):
                    people_dict[people_dict[CPR][6][i]] = [None, None, None, None, None, None, None, None, CPR]

print(people_dict[230226-9781])