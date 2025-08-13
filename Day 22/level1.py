import requests
from bs4 import BeautifulSoup
import json
#
url = 'https://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

content = response.content
soup = BeautifulSoup(content, 'html.parser') 


"""print(soup.title.get_text())
print(soup.body) 
print(response.status_code)
print(soup.title.get_text()) """

dictionary = {}
dic_len_3 = {}
dic_len_5 = {}
section = soup.find_all('section', {"class" : "stat-section" }) 

for i in section:
    name = i.find("h4")
    dictionary[i.find("h4").get_text()] = []
    for j in i.find("ul").find_all("li"):
        line =list([k.get_text() for k in j.find_all("span", recursive=False)])
        line_= {str(line[0]) : line[1]}

        dictionary[str(i.find("h4").get_text())].append(line_)


#print(len(section))
#print(dictionary)
#print(dictionary["Community"][0][1])  

div = soup.find_all("div", {"class" : "bu-stat-inner js-bu-stat-inner"})
h4 = soup.find_all("h4", {"class" : "stat-group-title"})
#print(len(div)) I found the solution with this line
for i in div:
    key = i.find("h3", {"class" : "bu-stat-title"}).get_text()
    parent_div = i.find_all("span")
    text_list = list(dict.fromkeys([i.get_text(strip =True) for i in parent_div]))
    value = "".join(text_list)

    if div.index(i) <= 2:
        dic_len_3[key.replace("\n","").replace("\t","")] = value
        dictionary[h4[0].get_text()] = dic_len_3
    else:
        dic_len_5[key.replace("\n","").replace("\t","")] = value
        dictionary[h4[2].get_text()] = dic_len_5



json_str = json.dumps(dictionary)
#print(json_str)
with open("info.json", "w") as f:
    json.dump(dictionary, f, indent=4)