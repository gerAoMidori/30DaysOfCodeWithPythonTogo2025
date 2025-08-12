import re
import json
#1
def Read(filename):
    with open(filename, "r") as f :
        info = f.read()
    words = len(re.findall("\\w+", info))
    lines = len(re.findall("\n", info))
    return lines, words

#print(Read("donald_speech.txt"))
#print(Read("obama_speech.txt"))

#2
def most_spoken_languages(filename, top):
    with open(filename, "r", encoding="utf-8") as f:
        loaded_data = json.loads(f.read())
    languages_extended = [j for i in loaded_data if "languages" in i for j in i["languages"] ]
    set_of_languages = set(languages_extended)
    unsorted_result = [(languages_extended.count(i), i) for i in set_of_languages]

    return sorted(unsorted_result, key = lambda x : x[0], reverse=True)[:top]

#print(most_spoken_languages("countries_data.json", 4))

#3
def most_populated_countries(filename, top):
    with open(filename, "r", encoding="utf-8") as f:
        loaded_data = json.loads(f.read())
    pop_list= [{"country": i["name"], "population": i["population"]} for i in loaded_data]
    return sorted(pop_list, key = lambda x : x.get("population"), reverse=True)[:top]

print(most_populated_countries("countries_data.json", 3))