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
    # Counting age distribution
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
        if people_dict[keys][10] == "woman":    # Counts number of women
            gender_distribution["woman"] += 1

        if people_dict[keys][10] == "man":      # Counts number of men
            gender_distribution["man"] += 1
    return gender_distribution

def first_time_parent(people_dict, gender):

    """
    Function that takes people_dict and gender string (either "man" or "woman") and calculates the average age for
    first time parents and min age, max age and average age for first time parents.

    Parameters
    ----------
    people_dict: dict
        CPR numbers are keys, each with a list of values describing information about each key.

    Returns
    -------
        - Age dict with parents CPR and count of ages when they became parents for the first time (shown in interval counts)
        - Age of youngest first time parent
        - Age of oldest first time parent
        - Average age of first time parents
    """
    age_dict = {"15-19":0, "20-24":0, "25-29":0, "30-34":0, "35-39":0,
                "40+":0, "Min":0, "Max":0, "Avg":0}
    min_age = 100 #theoretically should be set to max age
    max_age = 0
    age_sum = 0
    gender_count = 0

    for key in people_dict.keys():
        # Filtering for gender and people with kids
        if people_dict[key][10] == gender and people_dict[key][6] is not None:

            age_list = []
            gender_count += 1

            # Makes list of childrens age
            for i in people_dict[key][6]:
                age_list.append(people_dict[i][9])

            # Calculates the age of the parent, when having their first child
            age = int(people_dict[key][9]) - int(max(age_list))
            age_sum += age

            # Finds max and min age
            if age >= max_age:
                max_age = age
            if age <= min_age:
                min_age = age

            # Makes distribution of age
            if age >= 15 and age < 20:
                age_dict["15-19"] += 1
            if age >= 20 and age < 25:
                age_dict["20-24"] += 1
            if age >= 25 and age < 30:
                age_dict["25-29"] += 1
            if age >= 30 and age < 35:
                age_dict["30-34"] += 1
            if age >= 35 and age < 40:
                age_dict["35-39"] += 1
            if age >= 40:
                age_dict["40+"] += 1

    # Calculates the average age, and adds min, max and avg to age_dict
    avg_age = age_sum / gender_count
    age_dict["Min"] = min_age
    age_dict["Max"] = max_age
    age_dict["Avg"] = avg_age

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
            if people_dict[keys][6] is None:        # Counts childless women
                childless_dict["woman"] += 1
                childless_dict["all"] += 1
        elif people_dict[keys][10] == "man":
            count_all += 1
            count_men += 1
            if people_dict[keys][6] is None:        # Counts childless men
                childless_dict["man"] += 1
                childless_dict["all"] += 1

    # Calculates procentage of childless men, woman and all
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
        # If person has children
        if people_dict[keys][6] is not None:
            for kids in people_dict[keys][6]:
                # If children has children
                if people_dict[kids][6] is not None:
                    for element in people_dict[kids][6]:
                        # Adds key to grandparent_dict with grandchildren as values
                        if keys not in grandparent_dict:
                            grandparent_dict[keys] = [element]
                        # Adds grandchildren as values to the grandparent key
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
        # If grandparent has over 1 grandchildren
        if len(grandparent_dict[keys]) > 1:
            for i in range(len(grandparent_dict[keys])):
                # Add number of cousins to cousins_list
                if cousins_kid != 0:
                    cousins_list.append(cousins_kid)
                    cousins_kid = 0
                kid = grandparent_dict[keys][i]
                for j in range(len(grandparent_dict[keys])):
                    # If grandchildren has different parents, count cousins
                    if people_dict[kid][7] != people_dict[grandparent_dict[keys][j]][7] and people_dict[kid][8] != people_dict[grandparent_dict[keys][j]][8]:
                        cousins_kid += 1

    # Calculates the average number of cousins
    average_cousins = sum(cousins_list)/len(cousins_list)

    return average_cousins

def firstborn_gender_likelyhood(people_dict):
    """
    Function which takes people_dict and returns a list with the probability of the firstborn being male or female, respectively.

    Parameters
    ---------
    people_dict : dict
          CPR numbers as keys

    Returns
    -------
    List with probabilities: [probability of firstborn being male, probability of firstborn being female]

    """
    man_count = 0
    woman_count = 0
    children_count = 0

    for key in people_dict.keys():
        if people_dict[key][6] is not None:
            children_count += 1

            #construct new dict for children with age and gende
            children_dict = {}

            for i in people_dict[key][6]:
                children_dict[i] = [people_dict[i][9], people_dict[i][10]]

            # Finds the oldest child
            oldest_child = children_dict[max(children_dict, key = children_dict.get)]

            # Add count depending on gender
            if oldest_child[-1] == "woman":
                woman_count += 1
            if oldest_child[-1] == "man":
                man_count += 1

    #The probability of the firstborn being a male:
    man_prob = (man_count / children_count) * 100

    #The probability of the firstborn being a female
    woman_prob = (woman_count / children_count) * 100

    return [man_prob, woman_prob]



def multiple_partner(people_dict):
    """_summary_

    Args:
        people_dict (_type_): _description_

    Returns:
        _type_: _description_
    """
    man_count = 0
    woman_count = 0
    parents_dict_female = {} #construct dict with parents
    parents_dict_male = {}

    #calculate if two different children have the same mother but different father
    for key in people_dict.keys():
        if people_dict[key][7] and people_dict[key][8] is not None: #make sure that father and mother is present
            
            # Checks if mother has kids with another partner
            if people_dict[key][7] in parents_dict_female: 
                if parents_dict_female[people_dict[key][7]] != people_dict[key][8]:
                    woman_count += 1

            # Adds mother to dict with father as value
            if people_dict[key][7] not in parents_dict_female: 
                parents_dict_female[people_dict[key][7]] = people_dict[key][8]

            # Checks if father has kids with another partner
            if people_dict[key][8] in parents_dict_male: 
                if parents_dict_male[people_dict[key][8]] != people_dict[key][7]:
                    man_count += 1

            # Adds father to dict with mother as value
            if people_dict[key][8] not in parents_dict_male: 
                parents_dict_male[people_dict[key][8]] = people_dict[key][7]

    return [woman_count, man_count]


def tall_marriage(people_dict):
    """
    Function that calculates percentages of different marriages by height combinations of couples.
    Assumptoin: every couple that has at least one child have been/are married.

    Constraints for tall, normal and short in women and men:
    men:
        tall: > 185cm
        normal: 175 > and < 185cm
        short: < 175cm
    women:
        tall: >= 175cm
        normal: 165 >= and < 175cm
        short: < 165cm

    Parameters
    ---------
    people_dict : dict
          CPR numbers as keys

    Returns
    -------
    Dict with percantages of couples height combinations.

    """

    #initialization
    tall_tall = 0
    normal_normal = 0
    short_short = 0
    tall_short = 0
    normal_short = 0
    tall_normal = 0
    total = 0

    height_dict_male = {"Tall" : 0, "Normal" : 0, "Short": 0}
    height_dict_female = {"Tall" : 0, "Normal" : 0, "Short" : 0}
    
    tall_male = []
    tall_female = []
    normal_male = []
    normal_female = []
    
    #convert height values to integers
    for key, value in people_dict.items():
        people_dict[key][2] = int(value[2])
        
    #count height combinations
    for key in people_dict.keys():
        if people_dict[key][7] and people_dict[key][8] is not None:
            total += 1

            #tall/tall
            if people_dict[people_dict[key][7]][2] >= 175 and people_dict[people_dict[key][8]][2] >= 185:
                tall_tall += 1
                
                #extract height of child 
                if people_dict[key][10] == "man":
                    if people_dict[key][2] >= 185: 
                        height_dict_male["Tall"] += 1
                    if people_dict[key][2] < 185 and people_dict[key][2] >= 175: 
                        height_dict_male["Normal"] += 1
                    if people_dict[key][2] < 175: 
                        height_dict_male["Short"] += 1
                    
                    tall_male.append(people_dict[key][2])
                    
                if people_dict[key][10] == "woman":
                    if people_dict[key][2] >= 175: 
                        height_dict_female["Tall"] += 1
                    if people_dict[key][2] < 175 and people_dict[key][2] >= 165: 
                        height_dict_female["Normal"] += 1
                    if people_dict[key][2] < 165: 
                        height_dict_female["Short"] += 1     
                    
                    tall_female.append(people_dict[key][2])  
                    
            #normal/normal
            if (people_dict[people_dict[key][7]][2] < 175 and people_dict[people_dict[key][7]][2] >= 165) and (people_dict[people_dict[key][8]][2] < 185 and people_dict[people_dict[key][8]][2]) >= 175:
                normal_normal += 1
                
                if people_dict[key][10] == "man":
                    normal_male.append(people_dict[key][2])
                
                if people_dict[key][10] == "woman": 
                    normal_female.append(people_dict[key][2])
                
                
            #short/short
            if people_dict[people_dict[key][7]][2] < 165 and people_dict[people_dict[key][8]][2] < 175:
                short_short += 1

            #tall/short & short/tall
            if (people_dict[people_dict[key][7]][2] >= 175 and people_dict[people_dict[key][8]][2] < 175) or (people_dict[people_dict[key][7]][2] < 165 and people_dict[people_dict[key][8]][2]) >= 185:
                tall_short += 1
            
                if people_dict[key][10] == "man":
                    if people_dict[key][2] >= 185: 
                        height_dict_male["Tall"] += 1
                    if people_dict[key][2] < 185 and people_dict[key][2] >= 175: 
                        height_dict_male["Normal"] += 1
                    if people_dict[key][2] < 175: 
                        height_dict_male["Short"] += 1
                    
                if people_dict[key][10] == "woman":
                    if people_dict[key][2] >= 175: 
                        height_dict_female["Tall"] += 1
                    if people_dict[key][2] < 175 and people_dict[key][2] >= 165: 
                        height_dict_female["Normal"] += 1
                    if people_dict[key][2] < 165:
                        height_dict_female["Short"] += 1  
                            
            #tall/normal & normal/tall
            if (people_dict[people_dict[key][7]][2] >= 175 and (people_dict[people_dict[key][8]][2] >= 175 and people_dict[people_dict[key][8]][2] < 185)) or ((people_dict[people_dict[key][7]][2] < 175 and people_dict[people_dict[key][7]][2] >= 165) and people_dict[people_dict[key][8]][2] <= 185):
                tall_normal += 1
                
                if people_dict[key][10] == "man":
                    if people_dict[key][2] >= 185: 
                        height_dict_male["Tall"] += 1
                    if people_dict[key][2] < 185 and people_dict[key][2] >= 175: 
                        height_dict_male["Normal"] += 1
                    if people_dict[key][2] < 175: 
                        height_dict_male["Short"] += 1
                    
                if people_dict[key][10] == "woman":
                    if people_dict[key][2] >= 175: 
                        height_dict_female["Tall"] += 1
                    if people_dict[key][2] < 175 and people_dict[key][2] >= 165: 
                        height_dict_female["Normal"] += 1
                    if people_dict[key][2] < 165: 
                        height_dict_female["Short"] += 1  
                            
            #normal/short & short/normal
            if ((people_dict[people_dict[key][7]][2] < 175 and people_dict[people_dict[key][7]][2] >= 165) and people_dict[people_dict[key][8]][2] < 175) or (people_dict[people_dict[key][7]][2] < 165 and (people_dict[people_dict[key][8]][2] < 185 and people_dict[people_dict[key][8]][2] >= 175)):
                normal_short += 1


    result_dict = {"tall/tall" : tall_tall / total * 100,
                   "normal/normal" : normal_normal / total * 100,
                   "short/short" : short_short / total * 100,
                   "tall/normal" : tall_normal / total * 100,
                   "tall/short" : tall_short / total * 100,
                   "normal/short" : normal_short / total * 100}

    
    return result_dict, height_dict_male, height_dict_female


def bmi_marriage(people_dict):
    """
    Function that calculates the percentages of couples based on BMI combinations; fat/fat, normal/normal, slim/slim, fat/slim, fat/normal & normal/slim.

    BMI intepretations:
    Slim: < 18.5 = slim
    Normal: >= 18.5 and < 25 = normal
    Fat: > 25 = fat

    BMI calculation: weight / (height/10)^2 (height needs to be in meters)

    Parameters
    ---------
    people_dict : dict
          CPR numbers as keys

    Returns:
        BMI_dict : dict
            children as keys and their respective parents' BMI as values.
    """

    #initialization
    fat_fat = 0
    normal_normal = 0
    slim_slim = 0
    fat_normal = 0
    fat_slim = 0
    normal_slim = 0

    #dict with children as key and parents' BMI as values ([mother BMI, father BMI])
    BMI_dict = {}

    #convert height and weight to integers, calculate BMI and add to BMI dict
    for key, value in people_dict.items():
        if people_dict[key][7] and people_dict[key][8] is not None:
            BMI_dict[key] = [int(people_dict[people_dict[key][7]][3]) / float((int(people_dict[people_dict[key][7]][2]) / 100)**2),
                            int(people_dict[people_dict[key][8]][3]) / float((int(people_dict[people_dict[key][8]][2]) / 100)**2)]


    #counts couples based on BMI combination:
    for key, value in BMI_dict.items():
        if value[0] > 25 and value[1] > 25:
            fat_fat += 1
        elif value[0] < 18.5 and value[1] < 18.5:
            slim_slim += 1
        elif (value[0] < 25 and value[0] >= 18.5) and (value[1] < 25 and value[1] >= 18.5):
            normal_normal += 1
        elif (value[0] > 25 and (value[1] < 25 and value[1] >= 18.5)) or (value[1] > 25 and (value[0] < 25 and value[0] >= 18.5)):
            fat_normal += 1
        elif (value[0] > 25 and value[1] < 18.5) or (value[1] > 25 and value[0] < 18.5):
            fat_slim += 1
        elif (value[0] < 18.5 and (value[1] < 25 and value[1] >= 18.5)) or (value[1] < 18.5 and (value[0] < 25 and value[0] >= 18.5)):
            normal_slim += 1

    #contructs final dict w. every bmi combination (combinaiton as key, count as values)
    result_dict = {"fat/fat" : fat_fat / len(BMI_dict) * 100,
                   "slim/slim" : slim_slim / len(BMI_dict) * 100,
                   "normal/normal" : normal_normal / len(BMI_dict) * 100,
                   "fat/slim" : fat_slim / len(BMI_dict) * 100,
                   "fat/normal" : fat_normal / len(BMI_dict) * 100,
                   "normal/slim" : normal_slim / len(BMI_dict) * 100}

    return result_dict


# Function for exercise 15
def notRealParent(people_dict):
    """
    Function which takes people_dict and returns a list with the children with at least one non-biological parent

    Parameters
    ---------
    people_dict : dict
          CPR numbers as keys. Mother in position [7], father in position[8], Blood type in position [5]

    Returns
    -------
    bastard: List
    List with CPR of children with at least one non-biological parent
    """
    bastard = list()
    for key in people_dict.keys():

        # Skip person if both parents are not present
        if people_dict[key][8] == None or people_dict[key][7] == None:
            continue
        
        # Finds blood type of person, mother and father in people_dict
        childblood = people_dict[key][5]
        fatherblood = people_dict[people_dict[key][8]][5]
        motherblood = people_dict[people_dict[key][7]][5]

        # If person has blood, which is unheritaged from parents, add person to bastard list.
        if childblood[-1] == "+" and fatherblood[-1] == "-" and motherblood[-1] == "-":
            bastard.append(key)
        elif childblood[:-1] == "AB" and (fatherblood[:-1] != "AB" or motherblood[:-1] != "AB"):
            if fatherblood[:-1]+motherblood[:-1] not in (["AB", "BA"]):
                bastard.append(key)
        elif childblood[:-1] != "O" and childblood[:-1] not in fatherblood and childblood[:-1] not in motherblood:
            bastard.append(key)

    return bastard


# fatherDonatefor exercise 16
def fatherSonDonate(people_dict):
    """
    Function which takes people_dict as input and returns a list with fathers who can donate blood to their sons

    Parameters
    ------------
    people_dict: dict
    dict with cpr as keys, children in position[6], blood type in position[5], gender in position[10]

    Return
    --------
    father_donate: List
    List with a list of father(Who can donate), sons(Who can receive), and their bloodtype: [father, [children], [blood types]]
    """
    father_donate = list()
    son_receive = list()
    for key in people_dict.keys():
        son_receive = list()
        father_blood = people_dict[key][5]
        bloodtype = [father_blood]
        # Skips person if person has no children
        if people_dict[key][6] is None or people_dict[key][10] == "man":
            continue
        else:
            for child in people_dict[key][6]:
                # Skips child if child is not a man
                if people_dict[child][10] == "woman":
                    continue
                else:
                    child_blood = people_dict[child][5]
                    # Adds sons and blood types if father can donate blood to son
                    if father_blood[-1] == "-" or child_blood[-1] == "+":
                        if (father_blood[:-1] == "O" or child_blood[:-1] == "AB") or (father_blood[:-1] == "A" and child_blood[:-1] == "A") or (father_blood[:-1] == "B" and child_blood[:-1] == "B"):
                            son_receive.append(child)
                            bloodtype.append(child_blood)
        # If sons can receive the blood add the father, sons and blood types to the list
        if son_receive != []:
            father_donate.append([key,son_receive,bloodtype])
    return father_donate

# Function for exercise 17:
def grandchildDonate(grandparent_dict, people_dict):
    """
    Function which takes two dicts, one with grandparents as keys and grandchildren as values and people_dict
    It returns a list of grandparent there can receive blood, grandchildren there can donate blood and their blood type.

    Parameters
    -----------
    grandparent_dict: dict
    dict with grandparents cpr as keys and their grandchildren in a list as values

    people_dict: dict
    dict with cpr as keys and bloodtype in position[5]

    Returns
    --------
    receive_donate_blood: list
    a list with grandparents(receivers), grandchildren(donaters) and bloodtypes: [grandparent, [grandchildren], [bloodtype]]
    """
    receive_donate_blood = list()
    for key in grandparent_dict.keys():
        grandchild_donate = list()
        grandparent_blood = people_dict[key][5]
        bloodtype = [grandparent_blood]

        # Iterate over grandchildren
        for child in grandparent_dict[key]:
            child_blood = people_dict[child][5]

            # If grandchild can donate to grandparent, save child and blood type in lists
            if child_blood[-1] == "-" or grandparent_blood[-1] == "+":
                if (child_blood[:-1] == "O" or grandparent_blood[:-1] == "AB") or (child_blood[:-1] == "A" and grandparent_blood[:-1] == "A") or (child_blood[:-1] == "B" and grandparent_blood[:-1] == "B"):
                    grandchild_donate.append(child)
                    bloodtype.append(child_blood)
        
        # If any of the grandchildren can donate add grandparent, grandchildren and blood type to list
        if grandchild_donate != []:
            receive_donate_blood.append([key,grandchild_donate,bloodtype])
    return receive_donate_blood
