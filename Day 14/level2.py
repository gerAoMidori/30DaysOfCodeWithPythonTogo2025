from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark','Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
countries_upper = list(map(lambda x : x.upper(), countries))

#2
squared_numbers = list(map(lambda x : x**2, numbers))

#3
names_upper = list(map(lambda x : x.upper(), names))

#4
countries_land = list(filter(lambda x : "land" in x, countries))

#5
countries_six = list(filter(lambda x : len(x) == 6, countries))

#6
countries_six_more = list(filter(lambda x : len(x) >= 6, countries))

#7
countries_start_e = list(filter(lambda x : x[0] == "E", countries))

#8
create_name_wiht_a = reduce(lambda x, y : x + y, filter(lambda x : x[0] == "A", map(lambda x : x.upper()[:2], names)))

#9
def get_string_lists(my_list : list):
    return list(filter(lambda x : isinstance(x, str) , my_list))

#10
sum_numbers = reduce(lambda x, y : x + y, numbers)

#11
concatenate_countries = reduce(lambda x, y : x + ", " + y, countries)
sentence = f"{concatenate_countries} are north European countries"

#12
from countries_list import countries_list

def categorize_countries(pattern):
    return list(filter(lambda x : pattern in x, countries_list))

#print(categorize_countries("stan"))

#13
def start_character_dico():
    dico = {}
    for i in countries_list:
        dico[i[0]] = dico.get(i[0], 0) + 1
    return dico

#14
def get_first_ten_countries():
    return countries_list[:10]

#15
def get_last_ten_countries():
    return countries_list[-10:]
