#initalizing the board
board=[
   ['','',''],
   ['','',''],
   ['','','']
]

current_player='X'
game_over=True

#to design board 
def display_board():
    for row in board:
        print(" " "|".join(row))
        print("-"*5)
       
#to check wining status of current player
def check_win(current_player):
    for i in range(3):
  
        #check for every row that is X X X or O O O
        if all(board[i][j] == current_player for j in range(3)):
            return True
        #check for every column that is  X X X or O O O
        if all(board[j][i]==current_player for j in range(3)):
            return True
        '''
        check for diagonally 
        x                   O  
           x        or,          O    
              x                        O
        and also to check opposite diagonal in every moves
        
        '''
        if all(board[i][i]==current_player for i in range(3) or board[i][2-i]==current_player for i in range(3)):
            return True
    return False
        
#main game
while game_over:
    display_board()
    while True:
        row=int(input("Enter the row index 0,1,2"))
        column=int(input("enter the column index 0,1,2"))

        # to check valid move

        if 0<=row <=2 and 0<=column <=2 and board[row][column]=="":
            board[row][column]=current_player
            break
        else:
            print("Invalid move try again!")
    
    if check_win(current_player) is True:
        display_board()
        print(f"{current_player}wins!!")
        game_over = False
    elif all(board[i][j]!="" for i,j in range(3)):
        display_board()
        print("Tie!! Try with extra logic:")
        game_over=False
