from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7]+'  |'+board[8]+'  |'+board[9])
    
    
    print('---------')
    print(board[4]+'  |'+board[5]+'  |'+board[6])
    print('---------')
   
    print(board[1]+'  |'+board[2]+'  |'+board[3])


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():
    marker = ''
    while marker!='x' and marker!='o':
        marker = input(' choose x or o: ')
        player1 = marker
    if player1=='x':
        player2='o'
    else:
        player1='o'
        player2='x'
    return(player1,player2)

player1_marker,player2_marker = player_input()

def place_marker(board, marker, position):
    
    board[position] = marker

type(test_board)

place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board, marker):
    
    
           return  ((board[1]==board[2]==board[3]==marker) or
           (board[4]==board[5]==board[6]==marker) or  
           (board[7]==board[8]==board[9]==marker) or
           (board[7]==board[5]==board[3]==marker) or
           (board[9]==board[5]==board[1]==marker))
                               
   
  


def choose_first():
    first = random.randint(1,2)
    if first==1:
        return 'player1'
    else:
        return 'player2'
    

def space_check(board, position):
    
    return board[position] == ''

def full_board_check(board):
    for i in range(1,10):
        
        if space_check(board,i):
            
            return False
        
        else:
            return True
    
def player_choice():
    position = 'wrong'
    num = ['1','2','3','4','5','6','7','8','9']
    while position not in num:
        position = input('enter the position:(1-9) ')
        if position not in num:
            print('invalid position')
    return int(position)
   
 
    
def replay():
    ans = ''
    
    while ans!='yes' or ans!='no':
        ans = input('do you want to play again: yes or no:  ')
        if ans=='yes':
            return True
        else:
            return False
            
   //main code
    
print('Welcome to Tic Tac Toe!')

while True:
    board = ['']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn+ ' will go first')
    play_game = input('ready to play: y or no   ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'player1':
            display_board(board)
            position = player_choice()
            board[position] = player1_marker
            display_board(board)
            if win_check(board, player1_marker):
                print('player1 WON')
                game_on = False
            elif full_board_check(board):
                print('TIE')
            else:
                turn = 'player2'
            
            
        else:
            turn = 'player2'
            display_board(board)
            position = player_choice()
            board[position] = player2_marker
            display_board(board)
            if win_check(board, player2_marker):
                print('player1 WON')
                game_on = False
            elif full_board_check(board):
                print('TIE')
            else:
                turn = 'player1'
            
            
            
            
                    
                    
    if not replay():
        break
    
            
                    
    
            
        
    
                
                
                
        
                
        
    
