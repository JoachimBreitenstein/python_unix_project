#! /usr/bin/env python3

import re
import sys
import math
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

    # Adding first name
    if line[0:10] == "First name":
        people_dict[CPR][0] = line[12:-1]

    # Adding last name
    if line[:9] == "Last name":
        people_dict[CPR][1] = line[11:-1]

    # Adding height
    if line[:6] == "Height":
        people_dict[CPR][2] = line[8:-1]

    # Adding weight
    if line[:6] == "Weight":
        people_dict[CPR][3] = line[8:-1]

    # Adding eye color
    if line[:9] == "Eye color":
        people_dict[CPR][4] = line[11:-1]

    # Adding blood type
    if line[:10] == "Blood type":
        people_dict[CPR][5] = line[12:-1]

    # Adding children, mother and father
    if line[:8] == "Children":
        people_dict[CPR][6] = re.findall(r'\d{6}\-\d{4}', line)
        for i in range(len(people_dict[CPR][6])):

            # If child is in people_dict add the father or mother
            if people_dict[CPR][6][i] in people_dict.keys():
                if people_dict[CPR][10] == "woman":
                    people_dict[people_dict[CPR][6][i]][7] = CPR
                if people_dict[CPR][10] == "man":
                    people_dict[people_dict[CPR][6][i]][8] = CPR

            # If child is not in people_dict, add key and mother or father
            else:
                if people_dict[CPR][10] == "woman":
                    people_dict[people_dict[CPR][6][i]] = [None, None, None, None, None, None, None, CPR, None, None, None]
                if people_dict[CPR][10] == "man":
                    people_dict[people_dict[CPR][6][i]] = [None, None, None, None, None, None, None, None, CPR, None, None]
infile.close()

#_______________________________________________________________________________________________________________________
outfile = open("people_results.txt", 'w')

taskbreak = "______________________________________________________________________________"

# 1. Age and gender distribution
# Age
age_dist = age_distribution(people_dict)
print("Age distribution\n", file=outfile)
print("Age\tCount", file=outfile)
for key, value in age_dist.items():
    print(key, value, sep="\t", file=outfile)
print(taskbreak, file=outfile)

#Gender
gender_dist = gender_distribution(people_dict)
print("Gender distribution\n", file=outfile)
print("Gender\tCount", file=outfile)
for key, value in gender_dist.items():
    print(key, value, sep="\t", file=outfile)
print(taskbreak, file=outfile)

# 2. min, max, avg of first time fathers
firstTimeFather = first_time_parent(people_dict, "man")
print("Minimum, maximun and average age for first time fathers\n", file=outfile)
print("The average age for first time fathers is:", "{:0.2f}".format(firstTimeFather["Avg"]), file=outfile)
print("The minimum age for first time fathers is:", firstTimeFather["Min"], file=outfile)
print("The maximum age for first time fathers is:", firstTimeFather["Max"], file=outfile)
print(taskbreak, file=outfile)

# 3. Age distribution of first time fathers
print("Age distribution of first time fathers\n", file=outfile)
print("Age\tCount", file=outfile)
for key, value in firstTimeFather.items():
    if key not in ["Min","Max","Avg"]:
        print(key, value, sep="\t", file=outfile)
print(taskbreak, file=outfile)

# 4. min, max, avg of first time mothers
firstTimeMother = first_time_parent(people_dict, "woman")
print("Minimum, maximun and average age for first time mothers\n", file=outfile)
print("The average age for first time mothers is:", "{:0.2f}".format(firstTimeMother["Avg"]), file=outfile)
print("The minimum age for first time mothers is:", firstTimeMother["Min"], file=outfile)
print("The maximum age for first time mothers is:", firstTimeMother["Max"], file=outfile)
print(taskbreak, file=outfile)


# 5. Age distribution of first time mothers
print("Age distribution of first time mothers\n", file=outfile)
print("Age\tCount", file=outfile)
for key, value in firstTimeMother.items():
    if key not in ["Min","Max","Avg"]:
        print(key, value, sep="\t", file=outfile)
print(taskbreak, file=outfile)

# 6. Percentage of men and woman without children
childless = childless_distribution(people_dict)
print("Distribution of men and women without children\n", file=outfile)
print("Gender\tPercentage", file=outfile)
for key, value in childless.items():
    print(key,"\t", "{:0.2f}".format(value),"%" , file=outfile)
print(taskbreak, file=outfile)

# 7. Average age difference between parents
print("Average age difference between parents with a common child\n", file=outfile)
print("The average age difference of parents with a common child is: ", "{:0.2f}".format(avg_age_diff(people_dict)), file=outfile)
print(taskbreak, file=outfile)

# 8. People with at least one grandparent alive
grandparent_dict = grandparent(people_dict)
grandparentAlive = grandparent_alive(grandparent_dict, people_dict)
print("People with at least one grandparent alive\n", file=outfile)
print("People with grandparents alive:", grandparentAlive[0], sep="\t\t", file=outfile )
print("Percentage of the total population:","\t", grandparentAlive[1], " %", sep="", file=outfile)
print(taskbreak, file=outfile)

# 9. Average number of cousins
cousin = cousins(grandparent_dict, people_dict)
print("Average number of cousins for people with cousins\n", file=outfile)
print("The average number of cousins for people with cousins is:", "{:0.2f}".format(cousin), file=outfile)
print(taskbreak, file=outfile)

# 10. Firstborn's gender
prop_gender = firstborn_gender_likelyhood(people_dict)
print("The likehood of the firstborn's gender\n", file=outfile)
print("Male:", "\t", "{:0.2f}".format(prop_gender[0]), " %", sep="", file=outfile)
print("Female:", "\t", "{:0.2f}".format(prop_gender[1]), " %", sep="", file=outfile)
print(taskbreak, file=outfile)

# 11. Men and women with children with different partners
more_partners = multiple_partner(people_dict)
print("Men and Women with children with different partners\n", file=outfile)
print("There are", more_partners[0], "women with children with different partners", file=outfile)
print("There are", more_partners[1], "men with children with different partners", file=outfile)
print(taskbreak, file=outfile)

# 12. Do tall people marry
tall_marriage_result = tall_marriage(people_dict)
print("Percentage of couples based on their heights\n", file=outfile)
print("Height\t\tPercent", file=outfile)
for key, value in tall_marriage_result[0].items():
    print(key, "\t", "{:0.2f}".format(value), " %", sep="", file=outfile)
print(taskbreak, file=outfile)

# 13. Do tall parents get tall children
print("Do tall people get tall children?\n", file=outfile)
print("Height of boys\tCount",file=outfile)
for key, value in tall_marriage_result[1].items():
    print(key, value, sep="\t\t", file=outfile)
print("\nHeight of girls\tCount", file=outfile)
for key, value in tall_marriage_result[2].items():
    print(key, value, sep="\t\t", file=outfile)
print(taskbreak, file=outfile)

# 14. Do fat people marry
bmi_marriage_result = bmi_marriage(people_dict)
print("Do fat people get fat children?\n", file=outfile)
print("Weight\t\tCount", file=outfile)
for key, value in bmi_marriage_result.items():
    print(key, "{:0.2f}".format(value), sep="\t", file=outfile)
print(taskbreak, file=outfile)

# 15. Does anyone have a not real parent according to bloodtype
notrealparent_list = notRealParent(people_dict)
print("Children with a not real parent according to their blood type\n", file=outfile)
if notrealparent_list == []:
    print("No one can safely be said to have a not real parent", file=outfile)
else:
    for child in notrealparent_list:
        print("child",file=outfile)
print(taskbreak, file=outfile)

# 16. Fathers there can donate blood to a son
father_donate = fatherSonDonate(people_dict)
count_son_receive = 0
for element in father_donate:
    count_son_receive += len(element[1])

print("Fathers there can donate blood to their sons\n", file=outfile)
print("Number of fathers there can donate blood:", len(father_donate), sep="\t", file=outfile)
print("Number of sons there can receive blood:", count_son_receive, sep="\t\t", file=outfile)
print(taskbreak, file=outfile)

# 17. Grandchildren there can donate blood to a grandparent
grandchild_donate = grandchildDonate(grandparent_dict, people_dict)
count_grandchild_donate = 0
for element in grandchild_donate:
    count_grandchild_donate += len(element[1])

print("Grandchildren there can donate blood to a grandparent\n", file=outfile)
print("Number of grandparents there can receive blood:", len(grandchild_donate), sep="\t", file=outfile)
print("Number of grandchildren there can donate blood:", count_grandchild_donate, sep="\t", file=outfile)
print(taskbreak, file=outfile)