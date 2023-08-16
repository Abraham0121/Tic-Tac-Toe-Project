board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('-'*9)

def take_input():
    row = int(input('Enter row (1-3): ')) - 1
    column = int(input('Enter column (1-3): ')) - 1
    return row, column

def is_valid_move(board, row, column):
    if 0 <= row < 3 and 0<= column < 3 and board[row][column] == ' ':
        return True
    return False


def check_win(board, current_player):
    """
    Checks to see if the player has won. Splits it up into 3 main cases: Horizontal, Vertical, Diagonal
    """

    #This checks for horizontal wins
    for i in range(3):
        j = 0
        print( board[i][j] ,  board[i][j+1] , board[i][j+2] )
        if board[i][j] == board[i][j+1] == board[i][j+2] == current_player:
            return True
    
    #This checks for vertical wins
    for j in range(3):
        i = 0
        if board[i][j] == board[i+1][j] == board[i+2][j] == current_player:
            return True
    
    #This checks for the forward slash diagonal win
    i = 0
    j = 0
    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == current_player:
        return True
    
    #This checks for the back slash diagonal win1
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        return True
    
    return False
    


def is_board_full(board):
    i = 0
    j = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def main():
    board = [[' ' for _ in range(3)]for _ in range(3)]
    current_player = 'X'

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")

        row, column = take_input()

        if is_valid_move(board, row, column):
            board[row][column] = current_player
            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                display_board(board)
                print("It's a draw!")
                break
            else:
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
        else:
            print('That was an invalid move please try again.')



main()