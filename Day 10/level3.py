#1
from countries import countries

for i in countries:
    if "land" in i:
        print(i)
#2 
fruits = ["banane", "orange", "mangue", "citron"]

for i in range(len(fruits)//2):
    fruits[i], fruits[-i-1] = fruits[-i-1], fruits[i]

# I discovered a new way to reverse a list but I'll stick with this method: fruits = fruits[::-1]

print(fruits)

#3
import json

# Loading the JSON data
with open('countries_data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    data = list(data)

languages = {}
for i in data:
    if "languages" in i:
        for j in i["languages"]:
            languages[j] = languages.get(j, 0) + 1
#print(languages)
print("Total number of languages:", len(languages))

#Sort (Discovered how to sort dictionariesbased on values)
sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
top_10_languages =  [i[0] for i in sorted_languages[:10]]
print("Top 10 languages spoken in the world:", top_10_languages) 

#Displaying the 10 most populous countries 

sorted_data_by_population = sorted(data, key=lambda x: x.get("population", 0), reverse=True)
top_10_by_population = [i['name']for i in sorted_data_by_population[:10]]
print("Top 10 most populous countries:", top_10_by_population)


