from board import make_board, loc
from player import Players, create_player
import re

def win_check():

    if loc["7"] == loc["8"] == loc["9"] or loc["4"] == loc["5"] == loc["6"] or loc["1"] == loc["2"] == loc["3"] or loc["7"] == loc["5"] == loc["3"] or loc["9"] == loc["5"] == loc["1"] or loc["8"] == loc["5"] == loc["2"] :
        print("We have a winner!")
        return True
    else:
        return False

def have_winner(move, player1, player2):
    have_winner = None

    if move > 4:
        have_winner = win_check()
    
    if have_winner:
        if move % 2 == 0:
            print(f"{player2.name} playing '{player2.symbol}' won!")
            return have_winner
        elif move % 2 == 1:
            print(f"{player1.name} playing '{player1.symbol}' won!")
            return have_winner

def replay():
    while True:
        ask_replay = input("Would you like to play again? Y or N: ")
        if ask_replay.lower() == 'y':
            return game()
            break
        elif ask_replay.lower() == 'n':
            print("Thank you for playing.")
            return exit()
            break
        else:
            print("Please select 'Y' or 'N' only.")
            continue

def game():

    player_move = 0

    print("Welcome to the TicTacToe game \'Kirby The Great\' created. This is a two(2) player game. Please enjoy!\n")                     
    make_board()
    
    player1, player2 = create_player()
    
    print(f'{player1.name} will play {player1.symbol} and {player2.name} will play {player2.symbol}')

    while True:

        while True:
            p1_pos = input(f"{player1.name}, please select your move in positions: ")
            if p1_pos.isdigit() == False or int(p1_pos) > 9:
                print("Please enter a number between 1 - 9.")
                continue
            elif loc[p1_pos] != " ":
                print('This place is taken. Please select a different position.')
                continue
            else:
                player_move += 1
                loc[p1_pos] = player1.symbol
                make_board()
                break
            
        check_1 = have_winner(player_move, player1, player2)
        if check_1:
            replay()
            

        while True:
            p2_pos = input(f"{player2.name}, please select your move in positions.")
            if p2_pos.isdigit() == False or int(p2_pos) > 9:
                print("Please enter a number between 1 - 9.")
                continue
            elif loc[p2_pos] != " ":
                print('This place is taken. Please select a different position.')
                continue
            else:
                player_move += 1
                loc[p2_pos] = player2.symbol
                make_board()
                break
        
        check_2 = have_winner(player_move, player1, player2)
        if check_2:
            replay()
            

        if player_move > 7 and (not check_1 and not check_2):
            print('It\'s a tie! No winner.')
            replay()

game()
#replay()