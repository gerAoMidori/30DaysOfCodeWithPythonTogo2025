from bs4 import BeautifulSoup
import requests
import json
import re

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

page_content = requests.get(url).content
soup = BeautifulSoup(page_content, "html.parser")

table =  soup.find("table").find_all("tbody")
head = soup.find("table").find_all("tr")[0].find_all("th")

#print(table)
head_chart = [re.sub("\\[[a-z0-9]+]", "", i.get_text(strip=True)) for i in head]
print(head_chart)

dictionary = {}

for i in table:
    data = [] 
    rows = i.find_all("tr")[1:]  # Skip the header row
    for row in rows:
        data.append(row.find("th").find("a").get_text(strip=True))
        cells = row.find_all("td")
        for i in range(len(cells)):
            if len(cells[i].find_all(["i", "a", "span"])) > 1:
                tags_list = cells[i].find_all(["i", "a", "span"])
                if cells[i].find("br"):
                    cells[i] = " ".join([tag.get_text(strip=True) for tag in tags_list]).strip()
                elif len(cells[i].find_all("hr")) > 0:
                    cells[i] = "-".join([tag.get_text(strip=True) for tag in tags_list]).strip()
                else:
                    cells[i] = "-".join([tag.get_text(strip=True) for tag in tags_list]).strip()
            else:
                cells[i] = cells[i].get_text(strip=True)

        data.extend([re.sub("\\ [[a-z0-9 ]+]", "", cell)  if cell != "" else  "" for cell in cells])
        data [1] = row.find("img").get("src")
        data.remove("")
        dictionary[data[0]] = {i[0]: i[1] for i in zip(head_chart, data)}
        data = []

with open("presidents.json", "w", encoding= 'utf-8') as f:
    json.dump(dictionary, f, ensure_ascii=False, indent=3)