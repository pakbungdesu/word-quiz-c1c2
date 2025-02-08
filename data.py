
import requests
import json

# ------------------ FUNCTION ------------------ #
def wordlist_dict(filename):
    """
    Clean text file, put it in dictionary
    Keys: word, meaning
    Return: A list of dictionary
    """

    with open(filename, "r") as file:
        final = []
        for line in file:
            line = line.replace(" â€“ ", ":")
            res = line.split(":")
            final.append({"word": res[0], "meaning": res[1][:-1]})
    return final


def request_data(wordlist):
    """
    Request data and store information in dictionary
    Argument: A list of dictionary of words with keys = word, meaning
    Keys: word, synonyms, antonyms
    Return: A list of dictionary
    """

    result = []
    for word in wordlist:
        api_url = f'https://api.api-ninjas.com/v1/thesaurus?word={word["word"]}'
        response = requests.get(api_url,
                                headers={'X-Api-Key': 'C11feCFK8Ex5oBaKpTySZQ==hDAXdZibO2bhLfad'})

        if response.status_code == requests.codes.ok:
            data = response.json()  # Parse response as JSON
            try:
                mydict = {"word": data["word"],
                          "meaning": word["meaning"],
                          "synonyms": data["synonyms"][:5],
                          "antonyms": data["antonyms"]}
                result.append(mydict)
            except Exception as e:
                print(f"Error parsing data: {e}")  # Handle unexpected errors
                pass
        else:
            print("Error:", response.status_code, response.text)
    return result


def writejson(filename, listdict):
    """Write final clean json from list of dictionary"""
    with open(filename, "w") as jsonf:
        json.dump(listdict, jsonf, indent=4)

    print(f"Data has been written to {filename}")


# ------------------ PROCESS ------------------ #

w1_list = wordlist_dict("word1.txt")
w2_list = wordlist_dict("word2.txt")

res1 = request_data(w1_list)
res2 = request_data(w2_list)

writejson('w1_data.json', res1)
writejson('w2_data.json', res2)
