#! /usr/bin/env python3

#TEMPLATE FOR FUNCTION DESCRIPTIONS
"""
Function which take a dna string as an input.
The function returns the reversed complement string with newlines for every 60 base pairs

Parameters
----------
DNA_seq : String
    string of the DNA

Returns
-------
result_string : string
    reversed complement string with newline every 60 bp
"""


# Age distribution for exercise 1
def age_distribution(people_dict):
    """
    Function which takes all the data from a dictonary and finds the age distribution.
    The result is a count dict with age intervals as keys and count as values

    Parameters
    ----------
    people_dict : dict
        CPR numbers as keys and list with age in position [9] as values.

    Returns
    -------
    age_dict : dict
        dict with age interval as keys and count as values
    """
    age_dict = {"0-9":0, "10-19":0, "20-29":0, "30-39":0, "40-49":0, "50-59":0, "60-69":0, "70-79":0, "80-89":0, "90-99":0, "100+":0 }
    for keys in people_dict.keys():
        age = people_dict[keys][9]
        if age < 10:
            age_dict["0-9"] += 1
        if age >= 10 and age < 20:
            age_dict["10-19"] += 1
        if age >= 20 and age < 30:
            age_dict["20-29"] += 1
        if age >= 30 and age < 40:
            age_dict["30-39"] += 1
        if age >= 40 and age < 50:
            age_dict["40-49"] += 1
        if age >= 50 and age < 60:
            age_dict["50-59"] += 1
        if age >= 60 and age < 70:
            age_dict["60-69"] += 1
        if age >= 70 and age < 80:
            age_dict["70-79"] += 1
        if age >= 80 and age < 90:
            age_dict["80-89"] += 1
        if age >= 90 and age < 100:
            age_dict["90-99"] += 1
        if age >= 100:
            age_dict["100+"] += 1
    return age_dict

# Gender distribution for exercise 1
def gender_distribution(people_dict):
    """
    Function which takes all the data from a dictonary and finds the gender distribution.
    The result is a dict with woman and man as keys and count as values

    Parameters
    ----------
    people_dict : dict
        CPR numbers as keys and list with gender in position [10] as values.

    Returns
    -------
    gender_dict : dict
        dict with woman and man as keys and count as values
    """
    gender_distribution = {"woman":0, "man":0}
    for keys in people_dict.keys():
        if people_dict[keys][10] == "woman":
            gender_distribution["woman"] += 1

        if people_dict[keys][10] == "man":
            gender_distribution["man"] += 1
    return gender_distribution

def first_time_parent(people_dict, gender):

    age_dict = {"0-9":0, "10-19":0, "20-29":0, "30-39":0, "40-49":0, "50-59":0, "60-69":0, "70-79":0, "80-89":0, "90-99":0, "100+":0 }
    min_age = 100 #theoretically should be set to max age
    max_age = 0
    age_sum = 0
    gender_count = 0

    for key in people_dict.keys():
        if people_dict[key][10] == gender and people_dict[key][6] is not None:

            age_list = []
            gender_count += 1

            for i in people_dict[key][6]:
                age_list.append(people_dict[i][9])

            age = int(people_dict[key][9]) - int(max(age_list))
            age_sum += age

            if age >= max_age:
                max_age = age
            if age <= min_age:
                min_age = age

            if age >= 10 and age < 20:
                age_dict["10-19"] += 1
            if age >= 20 and age < 30:
                age_dict["20-29"] += 1
            if age >= 30 and age < 40:
                age_dict["30-39"] += 1
            if age >= 40 and age < 50:
                age_dict["40-49"] += 1
            if age >= 50 and age < 60:
                age_dict["50-59"] += 1
            if age >= 60 and age < 70:
                age_dict["60-69"] += 1
            if age >= 70 and age < 80:
                age_dict["70-79"] += 1
            if age >= 80 and age < 90:
                age_dict["80-89"] += 1
            if age >= 90 and age < 100:
                age_dict["90-99"] += 1
            if age >= 100:
                age_dict["100+"] += 1

    avg_age = age_sum / gender_count

    if gender == "woman":
        print("The average age for first time mothers is:", avg_age)
        print("The minimum age for first time mothers is:", min_age)
        print("The maximum age for first time mothers is:", max_age)

    elif gender == "man":
        print("The average age for first time fathers is:", avg_age)
        print("The minimum age for first time fathers is:", min_age)
        print("The maximum age for first time fathers is:", max_age)

    return age_dict


def avg_age_diff(people_dict):
    """
    Function that calculates the average age difference between first time parents.

    Parameters
    ----------
    people_dict: dict
        CPR numbers are keys, each with a list of values describing information about each key. Index 7 = cpr of mother, Index 8 = CPR of father, Index 10 = age.

    Returns
    -------
        Average age of first time parents.
    """
    
    parents_count = 0
    age_diff_sum = 0

    #find people with a child in common --> iterate through people --> if people[key] in two entries --> calc average age (print)
    for key, value in people_dict.items():
        if value[7] and value[8] is not None:
            parents_count += 2

            #summing age diff of all parents
            age_diff_sum += abs(int(people_dict[value[7]][9]) - int(people_dict[value[8]][9]))

    return age_diff_sum / parents_count

# childless_distribution function for exercise 6
def childless_distribution(people_dict):
    """
    Function which takes all the data from a dictonary and finds the gender distribution.
    The result is a dict with woman and man as keys and percent of not having children as values

    Parameters
    ----------
    people_dict : dict
        CPR numbers as keys and list, with children in position [6] and gender in position [10], as values.

    Returns
    -------
    childless_dict : dict
        dict with woman and man as keys and count in percent as values
    """

    count_women = 0
    count_men = 0
    count_all = 0
    childless_dict = {"woman":0, "man":0, "all":0}
    for keys in people_dict.keys():
        if people_dict[keys][10] == "woman":
            count_women += 1
            count_all += 1
            if people_dict[keys][6] is None:
                childless_dict["woman"] += 1
                childless_dict["all"] += 1
        elif people_dict[keys][10] == "man":
            count_all += 1
            count_men += 1
            if people_dict[keys][6] is None:
                childless_dict["man"] += 1
                childless_dict["all"] += 1

    childless_dict["woman"] = childless_dict["woman"]/count_women * 100
    childless_dict["man"] = childless_dict["man"]/count_men * 100
    childless_dict["all"] = childless_dict["all"]/count_all* 100
    return childless_dict

# Function for exercise 8, 9, 17
def grandparent(people_dict):
    """
    Function which takes all the data from a dictonary.
    The function returns a dict with the grandcparents as keys and grandchildren as values

    Parameters
    ----------
    people_dict : dict
        CPR numbers as keys and children in position [6] in values

    Returns
    -------
    grandparent_dict : dict
        dict with grandparents as keys and list of grandchildren as values.
    """
    grandparent_dict = dict()

    for keys in people_dict:
        if people_dict[keys][6] is not None:
            for kids in people_dict[keys][6]:
                if people_dict[kids][6] is not None:
                    for element in people_dict[kids][6]:
                        if keys not in grandparent_dict:
                            grandparent_dict[keys] = [element]
                        if keys in grandparent_dict:
                            grandparent_dict[keys].append(element)

    return grandparent_dict

# Function for exercise 8
def grandparent_alive(grandparent_dict, people_dict):
    """
    Function which takes a dict with grandparents as keys and grandchildren as values, and the dict with the whole dataset
    The function returns a list with number of grandchildren in position [0] and percentage of people with grandparent in position [1]

    Parameters
    ----------
    grandparent_dict: dict
        Grandparents as keys and their grandchildren as values

    people_dict : dict
        CPR numbers as keys

    Returns
    -------
     grandparent_alive: list
        list with number of people with a grandparent alive as position [0] and percent of the total people in position [1]
    """

    # Finds the number of people in the dict
    total_people = len(people_dict)

    # Makes a set of all the grandchildren
    grandchildren = set()
    for keys in grandparent_dict.keys():
        for element in grandparent_dict[keys]:
            grandchildren.add(element)

    # makes list of people with grandparent alive and percent of total set
    grandparent_alive = [len(grandchildren), len(grandchildren)/total_people*100]

    return grandparent_alive

# Function for exercise 9
def cousins(grandparent_dict, people_dict):
    """
    Function which takes a dict with grandparents as keys and grandchildren as values, and the dict with the whole dataset
    The function returns a list with number of grandchildren in position [0] and percentage of people with grandparent in position [1]

    Parameters
    ----------
    grandparent_dict: dict
        Grandparents as keys and their grandchildren as values

    people_dict : dict
        CPR numbers as keys

    Returns
    -------
     cousins_average: float
        The average numbers of cousins
    """

    cousins_list = []
    cousins_kid = 0
    for keys in grandparent_dict:
        if len(grandparent_dict[keys]) > 1:
            for i in range(len(grandparent_dict[keys])):
                if cousins_kid != 0:
                    cousins_list.append(cousins_kid)
                    cousins_kid = 0
                kid = grandparent_dict[keys][i]
                for j in range(len(grandparent_dict[keys])):
                    if people_dict[kid][7] != people_dict[grandparent_dict[keys][j]][7] and people_dict[kid][8] != people_dict[grandparent_dict[keys][j]][8]:
                        cousins_kid += 1

    average_cousins = sum(cousins_list)/len(cousins_list)

    return average_cousins
