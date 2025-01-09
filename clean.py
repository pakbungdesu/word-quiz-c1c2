
import json

with open("c1_data.json", "r") as file:
    c1 = json.load(file)

with open("c1_data.json", "r") as file:
    c2 = json.load(file)


c1_dict = []
c2_dict = []
for ele in c1:
    yes = True
    if ele["synonyms"] != [] and ele["antonyms"] != []:
        if "" in ele["synonyms"]:
            yes = False
        if "" in ele["antonyms"]:
            yes = False
    else:
        yes = False

    if yes:
        c1_dict.append(ele)

for ele in c2:
    yes = True
    if ele["synonyms"] != [] and ele["antonyms"] != []:
        if "" in ele["synonyms"]:
            yes = False
        if "" in ele["antonyms"]:
            yes = False
    else:
        yes = False

    if yes:
        c2_dict.append(ele)


file_name = "c2_clean.json"
with open(file_name, "w") as json_file:
    json.dump(c2_dict, json_file, indent=4)

print(f"Data has been written to {file_name}")

file_name = "c1_clean.json"
with open(file_name, "w") as json_file:
    json.dump(c1_dict, json_file, indent=4)


print(f"Data has been written to {file_name}")
