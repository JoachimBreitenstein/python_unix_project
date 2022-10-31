#! /usr/bin/env python3

from curses import KEY_UNDO
import re
import sys
#from 01_func_file import *

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
# [First name, Last name, Height, Weight, Eye colour, Blood type, Children, Mother, Father, grand parents, Age, Gender]
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

#print(people_dict["050354-4664"])


#first time fatherhood 
#year: 2000

#iterate through all fathers ages and subtract age of oldest child from fathers age
for key in people_dict.keys(): 
    if people_dict[key][10] == "man" and people_dict[key][6] is not None: 
        
        age_list = []
        
        for i in people_dict[key][6]:
            age_list.append(people_dict[i][9])
        
        if int(people_dict[key][9]) - int(max(age_list)) > 10 
        print(int(people_dict[key][9]) - int(max(age_list)))

