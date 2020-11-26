loc = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " " , "8": " ", "9": " "}

def make_board():
    print('Below is the board and positions available.')
    print(loc["7"] + "|" + loc["8"] + "|" + loc["9"])
    print("-+-+-")
    print(loc["4"] + "|" + loc["5"] + "|" + loc["6"])
    print("-+-+-")
    print(loc["1"] + "|" + loc["2"] + "|" + loc["3"])

    positions = ('''These are the position options:
                         9 - for top left box
                         8 - for top mid box
                         7 - for top right box
                         6 - for mid left box
                         5 - for mid mid box
                         4 - for mid right box
                         3 - for low left box
                         2 - for low mid box
                         1 - for low right box ''')

    print(positions)

