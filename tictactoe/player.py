import re

class Players:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

def create_player():
    pattern = re.compile(r'[a-zA-Z0-9]')
    pattern_symbol = re.compile(r'x|o')

    while True:
        name1 = input('Enter player one name: ')
        mo = pattern.search(name1)
        if mo == None:
            print("Please enter a name (alpha-numeric only).")
            continue
        else:
            break
    
    while True:
        symbol_for_name1 = input('Will you play "X" or "O"? ').lower()
        mo_symbol = pattern_symbol.search(symbol_for_name1)
        if mo_symbol == None:
            print("Please select from 'X' or 'O' only.")
            continue
        else:
            break
    
    while True:
        name2 = input('Enter player two name: ')
        mo_2 = pattern.search(name2)
        if mo_2 == None:
            print("Please enter a name (alpha-numeric only).")
            continue
        else:
            break
    
    symbol_for_name2 = ''
    if symbol_for_name1 == "o":
        symbol_for_name2 = "x"
    elif symbol_for_name1 == "x":
        symbol_for_name2 == "o"

    player1 = Players(name1, symbol_for_name1)
    player2 = Players(name2, symbol_for_name2)

    return player1, player2