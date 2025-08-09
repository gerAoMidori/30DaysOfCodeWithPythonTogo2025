"""
Write a function which check if provided variable is a valid python variable
Go to the data folder and access the countries-data.py file.
Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
"""
#1
def is_prime(number):
    if number  in (0, 1):
        return "Enter a number differentes de 0"
    count = 2
    while count <= number:
        if number % 2 == 0 and number != count:
            return False
        count += 1
    return True
#2
def check_unique_item(my_list : list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if my_list[i] == my_list[j] and i != j:
                return "It's not a unique list"
    return "This is the good one"

#3
def check_same_data_type(my_list : list):
    our_type = type(my_list[0])
    for i in my_list:
        if not isinstance(i, our_type):
            return "They are not the same data type."
    return "All the items are the same data type"

#4

def check_is_valid(variable : str):
    try:
        if isinstance(int(variable[0]), int):
            return 'Not Valid'
    except:
        pass
    for i in ("."):
        if i in variable:
            return "Not Valid"
    return "Valid name"

#5
from countries_data import data

def most_spoken_languages(data, amount):
    languages = {}

    for i in data:
        if "languages" in i:
            for j in i["languages"]:
                languages[j] = languages.get(j, 0) + 1


    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    top_10_languages =  [i[0] for i in sorted_languages[:amount]]
    print(f"The top {amount} languages spoken in the world:", top_10_languages) 


def most_populated_countries(data, amount):
    sorted_data_by_population = sorted(data, key=lambda x: x.get("population"), reverse=True)
    top_10_by_population = [i['name']for i in sorted_data_by_population[:amount]]
    print(f"The top {amount} most populated countries:", top_10_by_population)

most_populated_countries(data, 10)