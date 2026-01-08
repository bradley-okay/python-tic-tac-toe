def print_board(board):
#this function will print a board represented as lists with seperators to show the grid.    
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
#Checks the rows, columns, and diagonals for a winning line, if winning line is found, returns 'true, otherwise will return 'false', indicating no winner has been found.
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_valid_input(prompt):
#This function makes sure the player enters a number between 1 and 3, and no invalid characters such as a letter.
    while True:
        try:
            user_input = int(input(prompt)) - 1
            if user_input in range(3):
                return user_input
            else:
                print("Input must be between 1 and 3..")
        except ValueError:
            print("Invalid input! Please enter a number..")

def tic_tac_toe():
#Starts the game as an empty board, initializing the loop.
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        while True:
            print_board(board)
            row = get_valid_input(f"Player {current_player}, enter row (1-3): ")
            col = get_valid_input(f"Player {current_player}, enter column (1-3): ")

            if board[row][col] != " ":
    #Checks that a selected position is empty, if position has been filled will print an invalid move.
                print("Oh no, position taken! Try again!")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"-----Player {current_player} wins!-----")
                break

            if all(board[i][j] != " " for i in range(3) for j in range(3)):
    #Checks the whole board to see if every position has been filled, if no lines found, will print a draw.
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
    #Switches the players between "X" and "O".   
        new_game = input("Do you want to play again? (yes/no): ")
    #Initizalises the loop to restart a game if the player types "yes", otherwise will end the game.
        if new_game.lower() != "yes":
            print("Thanks for playing!")
            break
    #Exits the loop and ends the game.
        else:
            print("Starting a new game!")  

if __name__ == "__main__":
    tic_tac_toe()





