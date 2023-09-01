import pygame, sys
pygame.init()
# Set up display
WINDOW_SIZE = 600
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE/ 6
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic-Tac-Toe")


board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]



def draw_board(board):
    # The following variables are very important for positioning the tic tac toe board in the right place
    start_x = (WINDOW_SIZE - CELL_SIZE * GRID_SIZE) / 2
    start_y = (WINDOW_SIZE - CELL_SIZE * GRID_SIZE) / 2

    # Draws the board by drawing 4 horizontal and vertical lines
    for i in range(GRID_SIZE + 1):
        pygame.draw.line(screen, (0, 0, 0), (start_x, start_y + i * CELL_SIZE), (start_x + CELL_SIZE * GRID_SIZE, start_y + i * CELL_SIZE), 3)
        pygame.draw.line(screen, (0, 0, 0), (start_x + i * CELL_SIZE, start_y), (start_x + i * CELL_SIZE, start_y + CELL_SIZE * GRID_SIZE), 3)


    # This bit of code is responsible for drawing the X's and the O's 
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 'X':
                x_center = start_x + j * CELL_SIZE + CELL_SIZE // 2
                y_center = start_y + i * CELL_SIZE + CELL_SIZE // 2
                pygame.draw.line(screen, (0, 0, 0), (x_center - CELL_SIZE // 4, y_center - CELL_SIZE // 4), (x_center + CELL_SIZE // 4, y_center + CELL_SIZE // 4), 2)
                pygame.draw.line(screen, (0, 0, 0), (x_center - CELL_SIZE // 4, y_center + CELL_SIZE // 4), (x_center + CELL_SIZE // 4, y_center - CELL_SIZE // 4), 2)
            elif board[i][j] == 'O':
                x_center = start_x + j * CELL_SIZE + CELL_SIZE // 2
                y_center = start_y + i * CELL_SIZE + CELL_SIZE // 2
                pygame.draw.circle(screen, (0, 0, 0), (x_center, y_center), CELL_SIZE // 2 - 20, 2)




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
    
def display_winner(current_player, font):
    winner_text = font.render(f"Player {current_player} wins!", True, (0, 0, 0))
    text_x = (WINDOW_SIZE - winner_text.get_width()) // 2  # Center the text horizontally
    text_y = WINDOW_SIZE - winner_text.get_height() # Bottom center of the screen
    screen.blit(winner_text, (text_x, text_y))
    pygame.display.flip()  # Update the display
    pygame.time.wait(2000)  # Pause for a few seconds to show the result




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

    font = pygame.font.Font(None, 36)

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                start_x = (WINDOW_SIZE - CELL_SIZE * GRID_SIZE) / 2
                start_y = (WINDOW_SIZE - CELL_SIZE * GRID_SIZE) / 2
                row = int((y - start_y) // CELL_SIZE)
                column = int((x - start_x) // CELL_SIZE)


                if is_valid_move(board, row, column):
                    board[row][column] = current_player
                    if check_win(board, current_player):
                        draw_board(board)
                        display_winner(current_player, font)
                        game = False
                        break
                    elif is_board_full(board):
                        draw_board(board)
                        print("It's a draw!")
                        break
                    else:
                        if current_player == 'X':
                            current_player = 'O'
                        else:
                            current_player = 'X'

        screen.fill((255, 255, 255))
        
        player_text = font.render(f"Current Player: {current_player}", True, (0, 0, 0))
        screen.blit(player_text, (10, 10))  # Adjust the position as needed





        draw_board(board)  # Draw the current state of the board
        pygame.display.flip()  # Update the display




main()