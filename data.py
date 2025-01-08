import requests as rq
import pandas as pd
import json


df = pd.read_csv("octanove-vocabulary-profile-c1c2-1.0.csv")
word_list = df.to_dict(orient="records")
word_list = [{"headword": ele["headword"], "CEFR": ele["CEFR"]} for ele in word_list]
c2_list = [ele["headword"] for ele in word_list if ele["CEFR"] == "C2"]
c1_list = [ele["headword"] for ele in word_list if ele["CEFR"] == "C1"]

c2_data = []
c1_data = []

# ------------------------- C2 Part ------------------------- #

# Request information
for word in c2_list:
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
    response = rq.get(api_url, headers={'X-Api-Key': 'C11feCFK8Ex5oBaKpTySZQ==hDAXdZibO2bhLfad'})

    if response.status_code == rq.codes.ok:
        data = response.json()
        try:
            my_dict = {"word": data["word"], "synonyms": data["synonyms"][:5], "antonyms": data["antonyms"]}
            c2_data.append(my_dict)
        except Exception as e:
            print(f"Error parsing data: {e}")  # Handle unexpected errors
            pass
    else:
        print("Error:", response.status_code, response.text)


# Specify the file name
file_name = 'c2_data.json'

# Writing the data to a JSON file
with open(file_name, 'w') as json_file:
    json.dump(c2_data, json_file, indent=4)

print(f"Data has been written to {file_name}")


# ------------------------- C1 Part ------------------------- #

# Request information
for word in c1_list:
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
    response = rq.get(api_url, headers={'X-Api-Key': 'C11feCFK8Ex5oBaKpTySZQ==hDAXdZibO2bhLfad'})

    if response.status_code == rq.codes.ok:
        data = response.json()
        try:
            my_dict = {"word": data["word"], "synonyms": data["synonyms"][:5], "antonyms": data["antonyms"]}
            c1_data.append(my_dict)
        except Exception as e:
            print(f"Error parsing data: {e}")  # Handle unexpected errors
            pass
    else:
        print("Error:", response.status_code, response.text)


# Specify the file name
file_name = 'c1_data.json'

# Writing the data to a JSON file
with open(file_name, 'w') as json_file:
    json.dump(c1_data, json_file, indent=4)

print(f"Data has been written to {file_name}")
