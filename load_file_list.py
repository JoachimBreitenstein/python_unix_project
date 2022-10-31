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

CPR_list = []
first_name_list = []
last_name_list = []
height_list = []
weight_list = []
eye_color_list = []
blood_type_list = []
children_list = []



for line in infile:
    if line[0] == "#":
        continue

    if line[:3] == "CPR" and len(CPR_list) != len(children_list):
        children_list.append("None")

    if line[:3] == "CPR":
        CPR = re.search(r'(\d{6}\-\d{4})', line)
        CPR_list.append(CPR.group(1))
    
    if line[0:10] == "First name":
        first_name_list.append(line[12:-1])
    
    if line[:9] == "Last name":
        last_name_list.append(line[11:-1])
    
    if line[:6] == "Height":
        height_list.append(line[8:-1])
    
    if line[:6] == "Weight":
        weight_list.append(line[8:-1])
    
    if line[:9] == "Eye color":
        eye_color_list.append(line[11:-1])
    
    if line[:10] == "Blood type":
        blood_type_list.append(line[12:-1])
    
    if line[:8] == "Children":
        children_list.append(re.findall(r'\d{6}\-\d{4}', line))
if len(CPR_list) != len(children_list):
    children_list.append("None")


print(CPR_list[4])
print(first_name_list[4])
print(last_name_list[4])
print(height_list[4])
print(weight_list[4])
print(eye_color_list[4])
print(blood_type_list[4])
print(children_list[4])