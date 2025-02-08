
import json

# ------------------ FUNCTION ---------------------- #
def loadjson(filename):
    """Load json from json file"""
    with open(filename, "r") as file:
        jsonf = json.load(file)
    return jsonf


def writejson(filename, listdict):
    """Write final clean json from list of dictionary"""
    with open(filename, "w") as jsonf:
        json.dump(listdict, jsonf, indent=4)
    print(f"Data has been written to {filename}")


# ------------------ PROCESS---------------------- #
w1 = loadjson("w1_data.json")
w2 = loadjson("w2_data.json")

w1 = [{"word": ele["word"], "meaning": ele["meaning"],
       "synonyms": ele["synonyms"], "antonyms": ele["antonyms"][:5]}
      for ele in w1 if ele["synonyms"] != [] and
      ele["antonyms"] != [] and
      "" not in ele["synonyms"] and
      "" not in ele["antonyms"]]

w2 = [{"word": ele["word"], "meaning": ele["meaning"],
       "synonyms": ele["synonyms"], "antonyms": ele["antonyms"][:5]}
      for ele in w2 if ele["synonyms"] != [] and
      ele["antonyms"] != [] and
      "" not in ele["synonyms"] and
      "" not in ele["antonyms"]]

writejson("w1_clean.json", w1)
writejson("w2_clean.json", w2)
