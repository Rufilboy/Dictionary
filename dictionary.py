import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        choice = input("Press y for yes or n for no: ")
        if choice == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif choice == "n":
            return("Unable to locate your search.")
        else:
            return("You have entered wrong input, cross-check it!!!")
    else:
        print("Unable to locate your search.")



word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
