#Paguio,Jarred
#42762868

import numpy as np
import random
import sys

#Setting up the board
board = np.arange(27).reshape(3,3,3)
board.fill(0)

#Instructions on how to fill board
print'Top board is 0. Middle board is 1. Bottom board is 2.'
print'Rows of each board from top to bottom is 0, 1, 2 respectively.'
print'Columns of each board from left to right is 0, 1, 2 respectively.'
print'For example, I want to replace the top board\'s center to be my mark. I would input 0 1 1. Take note of the spaces between each number.'
board[0,1,1] = 1
print board

#Reset board after example
board.fill(0)

#Choosing opponent
while True:
    opponent = raw_input("Do you want to play against a Player or AI? (Type 'Player' or 'AI') ")
    if opponent in ['Player','player']:
        print'You have chosen another person as your opponent.'
        break
    elif opponent in ['AI','ai','Ai']:
        print'You have chosen to go against the computer.'
        break
    print'Invalid input. Please type \'Player\' or \'AI\''

#Win conditions
def victory(v):
    #1
    if board[0,0,0] == v and board[0,0,1] == v and board[0,0,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #2
    if board[0,1,0] == v and board[0,1,1] == v and board[0,1,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #3
    if board[0,2,0] == v and board[0,2,1] == v and board[0,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #4
    if board[1,0,0] == v and board[1,0,1] == v and board[1,0,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #5
    if board[1,1,0] == v and board[1,1,1] == v and board[1,1,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #6
    if board[1,2,0] == v and board[1,2,1] == v and board[1,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #7
    if board[2,0,0] == v and board[2,0,1] == v and board[2,0,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #8
    if board[2,1,0] == v and board[2,1,1] == v and board[2,1,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #9
    if board[2,2,0] == v and board[2,2,1] == v and board[2,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #10
    if board[0,0,0] == v and board[0,1,0] == v and board[0,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #11
    if board[0,0,1] == v and board[0,1,1] == v and board[0,2,1] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #12
    if board[0,0,2] == v and board[0,1,2] == v and board[0,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #13
    if board[1,0,0] == v and board[1,1,0] == v and board[1,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #14
    if board[1,0,1] == v and board[1,1,1] == v and board[1,2,1] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #15
    if board[1,0,2] == v and board[1,1,2] == v and board[1,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #16
    if board[2,0,0] == v and board[2,1,0] == v and board[2,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #17
    if board[2,0,1] == v and board[2,1,1] == v and board[2,2,1] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #18
    if board[2,0,2] == v and board[2,1,2] == v and board[2,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #19
    if board[0,0,0] == v and board[1,0,0] == v and board[2,0,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #20
    if board[0,0,1] == v and board[1,0,1] == v and board[2,0,1] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #21
    if board[0,0,2] == v and board[1,0,2] == v and board[2,0,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #22
    if board[0,1,0] == v and board[1,1,0] == v and board[2,1,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #23
    if board[0,1,1] == v and board[1,1,1] == v and board[2,1,1] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #24
    if board[0,1,2] == v and board[1,1,2] == v and board[2,1,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #25
    if board[0,2,0] == v and board[1,2,0] == v and board[2,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #26
    if board[0,2,1] == v and board[1,2,1] == v and board[2,2,1] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #27
    if board[0,2,2] == v and board[1,2,2] == v and board[2,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #28
    if board[0,0,0] == v and board[0,1,1] == v and board[0,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #29
    if board[1,0,0] == v and board[1,1,1] == v and board[1,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #30
    if board[2,0,0] == v and board[2,1,1] == v and board[2,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #31
    if board[0,0,2] == v and board[0,1,1] == v and board[0,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #32
    if board[1,0,2] == v and board[1,1,1] == v and board[1,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #33
    if board[2,0,2] == v and board[2,1,1] == v and board[2,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #34
    if board[0,2,0] == v and board[1,2,1] == v and board[2,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #35
    if board[0,1,0] == v and board[1,1,1] == v and board[2,1,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #36
    if board[0,0,0] == v and board[1,0,1] == v and board[2,0,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #37
    if board[0,0,0] == v and board[1,1,1] == v and board[2,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #38
    if board[0,0,0] == v and board[1,1,0] == v and board[2,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #39
    if board[0,0,1] == v and board[1,1,1] == v and board[2,2,1] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #40
    if board[0,0,2] == v and board[1,1,2] == v and board[2,2,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #41
    if board[0,0,2] == v and board[1,1,1] == v and board[2,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #42
    if board[0,0,2] == v and board[1,0,1] == v and board[2,0,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #43
    if board[0,1,2] == v and board[1,1,1] == v and board[2,1,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #44
    if board[0,2,2] == v and board[1,2,1] == v and board[2,2,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #45
    if board[0,2,2] == v and board[1,1,1] == v and board[2,0,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #46
    if board[0,2,2] == v and board[1,1,2] == v and board[2,0,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #47
    if board[0,2,1] == v and board[1,1,1] == v and board[2,0,1] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #48
    if board[0,2,0] == v and board[1,1,0] == v and board[2,0,0] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()
    #49
    if board[0,2,0] == v and board[1,1,1] == v and board[2,0,2] == v:
        if v == 1:
            print'Player 1 wins!'
            sys.exit()
        if v == 2:
            if opponent in ['Player','player']:
                print'Player 2 wins!'
                sys.exit()
            elif opponent in ['AI','ai','Ai']:
                print'You lost!'
                sys.exit()

#Turn system
for i in range(27):
    if i == 0 or i % 2 == 0:
        while True:
            player1 = raw_input("Player 1: Where do you want to put a 1? (Depth Row Column) ")
            player1 = player1.split()
            if len(player1) == 3:
                a1 = player1[0]
                b1 = player1[1]
                c1 = player1[2]
                if a1 in ['0','1','2'] and b1 in ['0','1','2'] and c1 in ['0','1','2'] and board[a1,b1,c1] == 0:
                    board[a1,b1,c1] = 1
                    break
            print'Invalid input.'
    else:
        if opponent in ['Player','player']:
            while True:
                player2 = raw_input("Player 2: Where do you want to put a 2? (Depth Row Column) ")
                player2 = player2.split()
                if len(player2) == 3:
                    a2 = player2[0]
                    b2 = player2[1]
                    c2 = player2[2]
                    if a2 in ['0','1','2'] and b2 in ['0','1','2'] and c2 in ['0','1','2'] and board[a2,b2,c2] == 0:
                        board[a2,b2,c2] = 2
                        break
                print'Invalid input.'
        elif opponent in ['AI','ai','Ai']:
            while True:
                a2 = random.randint(0,2)
                b2 = random.randint(0,2)
                c2 = random.randint(0,2)
                if board[a2,b2,c2] == 0:
                    board[a2,b2,c2] = 2
                    break
    print'Turn',i+1
    print board
    v = 1
    victory(v)
    v = 2
    victory(v)
print'Cat\'s game!'
