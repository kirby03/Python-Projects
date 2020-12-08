import json

data = json.load(open("dictionary\data.json"))

def findMeaning(word):
    low_case_word = word.lower()
    if low_case_word in data.keys():
        print(data[low_case_word])
    elif low_case_word == 'x':
        return exit()
    else:
        print("Word does not exist. Please check if the spelling is correct.")

while True:
    entry = input("To search meaning, type word[type 'x' to exit]: ")
    findMeaning(entry)