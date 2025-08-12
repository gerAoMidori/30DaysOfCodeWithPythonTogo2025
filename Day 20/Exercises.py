import requests 
import statistics
import re
import json
import pandas as pd

url = "https://api.thecatapi.com/v1/breeds"
url_rj = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/refs/heads/master/data/romeo_and_juliet.txt"


#1
response_rj = requests.get(url_rj)
data_rj = response_rj.text
a = re.findall("\\w+", data_rj)
b = set(a)

get_common_word = [(a.count(i), i) for i in b]
common_word_sorted = sorted(get_common_word, key=lambda x : x[0], reverse=True)

romeo_and_juliet = [i[1] for i in common_word_sorted[: 10]]


#2
response = requests.get(url) 
data = json.loads(response.text)
def get_info_find(data_extaracted):
    
    data_converted = [list(map(int, i)) for i in data_extaracted]
    data_flattened = [j for i in data_converted for j in i]


    data_mean = statistics.mean(data_flattened)
    data_std = statistics.stdev(data_flattened)

    exported_data = {
        "min" : min(data_flattened),
        "max" : max(data_flattened),
        "mean" : data_mean, 
        "std_variation": data_std
        }
    return exported_data

def display_info(param, dico):
    print("*****************************")
    print("For the", param, ":")
    for i in dico:
        print(f"{i} is {dico[i]}")


#Weight 
#get_cats_weight =  [data[i]["weight"]["metric"].split(" - ") for i in range(len(data))]
get_cats_weight = [re.findall("\\d+", data[i]["weight"]["metric"]) for i in range(len(data))]

display_info("weight", get_info_find(get_cats_weight))

#life_span
get_cats_life_span= [re.findall("\\d+", data[i]["life_span"]) for i in range(len(data))]

display_info("life_span", get_info_find(get_cats_life_span))



#Breed and Country frequency table
#I don't know what I'm suppose to do 

data_for_table = {
    "origin" : [i["origin"] for i in data],
    "name" : [i["name"] for i in data]
}

df = pd.DataFrame(data_for_table)

frequency_table = pd.crosstab(df["origin"], df["name"])
print(frequency_table)

