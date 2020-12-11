import json
import difflib
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("dictionary\data.json"))

def spellCheck(w):
    return get_close_matches(w, data.keys(), cutoff=0.75)

def findMeaning(word):
    low_case_word = word.lower()
    title_word = word.title()
    caps_word = word.upper()
    if low_case_word in data.keys():
        for f in data[low_case_word]:
            print("\n- " + f)
    elif title_word in data.keys():
        for f in data[title_word]:
            print("\n- " + f)
    elif caps_word in data.keys():
        for f in data[caps_word]:
            print("\n- " + f)
    elif low_case_word == 'x':
        return exit()
    else:
        check = spellCheck(low_case_word)
        print("Word does not exist. Please check the spelling.")
        if check != []:
            print(f"Did you mean {check}?")

while True:
    entry = input("\nTo search definition, type word. (Type 'x' to exit.): ")
    findMeaning(entry)