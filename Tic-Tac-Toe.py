#!/usr/bin/env python
# coding: utf-8

# In[5]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+' |'+board[2]+'| '+board[3])
    print('-------')
    print(board[4]+' |'+board[5]+'| '+board[6])
    print('-------')
    print(board[7]+' |'+board[8]+'| '+board[9])
    

def check_row(board):
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        return True
    if board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        return True
    if board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        return True
    if board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        return True
    if board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        return True
    if board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        return True
    if board[1] == board[5] and board[5] == board[9] and board[1] != ' ':
        return True
    if board[3] == board[5] and board[5] == board[7] and board[3] != ' ':
        return True
    
    return False


def intro(num):
    if num == 0 or num.lower() == 'n' or num.lower() == 'no':
        print('Of course, Have a nice day!')
        return False
    if num == 1 or num.lower() == 'y' or num.lower() == 'yes':
        print('These are the rules of the game: ')
        print("The aim of this game is place 3 'X's or 3 'O's in a row")
        print('The grid is numbered as follows: ')
        print('1'+' |'+'2'+'| '+'3')
        print('-------')
        print('4'+' |'+'5'+'| '+'6')
        print('-------')
        print('7'+' |'+'8'+'| '+'9')
        print('pick the corresponding number to fill square')
        print('The player that gets 3 in a row first wins!')
        return True
    
def check_spot(board,spot):
    return board[spot] == ' '


# In[8]:


choice = input('Would you like to play a game of Tic-Tac-Toe: ')
so = intro(choice)
win = False
while so:
    print('player1 is X ')
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    spot = 0
    turn = 1
    while ' ' in test_board:
        if turn%2 == 0:
            spot = int(input('player2 your go: '))
            if check_spot(test_board,spot):
                test_board.pop(spot)
                test_board.insert(spot,'O')
            else:
                print('That is not an empty spot, pick again')
                turn -= 1
            print(test_board)
            display_board(test_board)
            if check_row(test_board):
                print('Congratulations! Player2 wins')
                win = True
                break
        else:
            spot = int(input('player1 your go: '))
            if check_spot(test_board,spot):
                test_board.pop(spot)
                test_board.insert(spot,'X')
            else:
                print('That is not an empty spot, pick again')
                turn -= 1
            print(test_board)
            display_board(test_board)
            if check_row(test_board):
                print('Congratulations! Player1 wins')
                win = True
                break
                
        turn += 1
    
    if win == False:
        print('It was a tie!')
    choice = input('Would you like to play again: ')
    so = intro(choice)


# In[39]:


test_board.insert(2,'X')


# In[40]:


test_board


# In[ ]:




