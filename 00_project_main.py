#! /usr/bin/env python3

import re
import sys
from func_file import *

if len(sys.argv) == 1:
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
# [First name[0], Last name[1], Height[2], Weight[3], Eye colour[4], Blood type[5], Children[6], Mother[7], Father[8], Age[9], Gender[10]]
people_dict = {}
for line in infile:

    if line[:3] == "CPR":
        # Finding CPR number
        cpr_search = re.search(r'(\d{6}\-\d{4})', line)
        CPR = cpr_search.group(1)

        # Finding age
        age = 100-int(CPR[4:6])

        # Finding the gender of the person
        if int(CPR[-1]) in [2,4,6,8]:
            gender = "woman"
        if int(CPR[-1]) in [1,3,5,7,9]:
            gender = "man"

        # Adding age and gender to dictionary
        if CPR not in people_dict.keys():
            people_dict[CPR] = [None, None, None, None, None, None, None, None, None, age, gender]
        else:
            people_dict[CPR][9] = age
            people_dict[CPR][10] = gender

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
        for i in range(len(people_dict[CPR][6])):

            if people_dict[CPR][6][i] in people_dict.keys():
                if people_dict[CPR][10] == "woman":
                    people_dict[people_dict[CPR][6][i]][7] = CPR
                if people_dict[CPR][10] == "man":
                    people_dict[people_dict[CPR][6][i]][8] = CPR

            else:
                if people_dict[CPR][10] == "woman":
                    people_dict[people_dict[CPR][6][i]] = [None, None, None, None, None, None, None, CPR, None, None, None]
                if people_dict[CPR][10] == "man":
                    people_dict[people_dict[CPR][6][i]] = [None, None, None, None, None, None, None, None, CPR, None, None]

#Distribution of first time parents
age_dict = first_time_parent(people_dict, "man")
for key in age_dict:
    print(key, ":", age_dict[key])


#what is the average age difference betweeen the parents
mean_age_diff = avg_age_diff(people_dict)
print("The average age difference between parents is:", mean_age_diff)

#what is the average number of cousins


#is the firstborn likely to be male of female


#How many men and women have children with more than one partner? 
