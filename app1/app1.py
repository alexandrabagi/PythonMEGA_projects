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
    elif len(get_close_matches(word, data.keys())) > 0:
        match = get_close_matches(word, data.keys())[0]
        yn = (input("Did you mean %s instead? Enter 'Y' if yes or 'N' if no: " % match)).lower()
        if yn == 'y':
            return data[match]
        elif yn == 'n':
            return "This word does not exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "This word does not exist. Please double check it."

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
