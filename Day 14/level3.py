from countries_data import data

def sort_by(key):
    sorted_data_by_ = sorted(data, key=lambda x: x.get(key), reverse=True)
    return sorted_data_by_


def sort_by_languages():
    languages = {}
    for i in data:
        if "languages" in i:
            for j in i["languages"]:
                languages[j] = languages.get(j, 0) + 1
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)

#1
print(sort_by("name"))
print(sort_by("capital"))
print(sort_by("population"))

#2
print(f"The 10 most spoken languages are {[i[0] for i in sort_by_languages()[:10]]}")

#3
print("The ten most populated countries :", [i["name"] for i in sort_by("population")[:10]])
