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
    
    parents_count = 0
    age_diff_sum = 0

    #find people with a child in common --> iterate through people --> if people[key] in two entries --> calc average age (print)
    for key, value in people_dict.items(): 
        if value[7] and value[8] is not None: 
            parents_count += 2
        
            #summing age diff of all parents
            age_diff_sum += abs(int(people_dict[value[7]][9]) - int(people_dict[value[8]][9]))
            
    return age_diff_sum / parents_count



