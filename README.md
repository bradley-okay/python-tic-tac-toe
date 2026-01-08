R4  -    
    - GitHub link - https://github.com/Bradley-ok
    - Slide deck link - https://youtu.be/dKg4nTSc4Rs


R5 - Code style guide is based on PEP8

R6 - Describe and list 3 features of the terminal app
- 3 key features i have included in my code to create a tic-tac-toe terminal app include, an interactive command line interface, the ability to take an input from a user and checks if a winner or tie has been found, and a function to ensure a valid character has been used for each players turn.

- In my app i have included code which will print a 3x3 grid to resemble a tic-tac-toe grid within the terminal. I used the join() method in order to take all items and join them into one string,  in this case i take all the "|" along with "-" * 9, as this worked out to be a good amount of dashes to fill the board. The interactive board is able to take users turns based of coordinates (rows and columns), in order to place either an "X" or "O". The board is then updated to display the current state of the game after each players turn.

- After a player has made a turn, the code then checks to see if any winner has been detected when a line has been formed in either a row, column or diagonal, with 3 of the same symbol. The code will return true if no winner has been found, and a false if a winning line has been made, and the winning player will then be displayed in the terminal. I have then included the option to either restart or quit the game, whether the player types "yes" or "no" to continue playing.

- Another feature i have included in the code, as a problem i found when testing the app was that it would give an error if an invalid characted was used, instead of a number between 1-3 for each row and column. The code utilizes the try and except block with a ValueError exception, allowing the player to retake their turn if an invalid character has been used, which creates a much better flow of the game.
