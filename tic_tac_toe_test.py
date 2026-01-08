from main import check_winner  # Imports the functions to be tested
import pytest

# Test check_winner function
def test_check_winner():
    # Test if check_winner correctly identifies a winning row for 'X'
    board = [
        ['X', 'X', 'X'],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    assert check_winner(board, 'X') == True
    # Test if check_winner correctly identifies a non-winning board state
    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['X', 'O', 'X']
    ]
    assert check_winner(board, 'X') == False
