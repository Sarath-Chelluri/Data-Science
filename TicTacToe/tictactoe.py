"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turn = 0
    for col in board:
        for val in col:
            if val == X:
                turn += 1
            elif val == O:
                turn -= 1
    return X if turn % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avaliable_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                avaliable_actions.add((i, j))
    return avaliable_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    new_board = copy.deepcopy(board)

    if action[0] > 2 or action[0] < 0 or action[1] > 2 or action[1] < 0:
        raise Exception("Invalid Move")

    if new_board[action[0]][action[1]] is not None:
        raise Exception("Invalid Move")

    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] is not None:
                return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] is not None:
                return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] is not None:
            return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] is not None:
            return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in board:
        if None in i:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    if winner(board) == None:
        return 0


def max_value(board):
    v = float("-inf")
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = float("inf")
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    optimal_action = None

    if current_player == "X":
        max_val = float("-inf")
        for action in actions(board):
            val = min_value(result(board, action))
            if val > max_val:
                max_val = val
                optimal_action = action
        return optimal_action

    min_val = float("inf")
    for action in actions(board):
        val = max_value(result(board, action))
        if val < min_val:
            min_val = val
            optimal_action = action
    return optimal_action
