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
    if terminal(board):
        return None
    countX=0
    countO=0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1
    if countX > countO:
        return O
    else:
        return X






def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None

    actions=[]
    for i in range(3):
        for j in range(3):
            if a[i][j] == EMPTY:
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    actions_set=actions(board)
    if action not in actions_set:
        raise Exception("Not a valid move")
    boardcopy = copy.deepcopy(board)
    i=action[0]
    j=action[1]
    user=player(board)
    boardcopy[i][j] = user
    return boardcopy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        countX=0
        countO=0
        for j in range(3):
            if a[i][j] == X:
                countX +=1
            if a[i][j] == O:
                countO +=1
        if countX==3:
            return X
        if countO==3:
            return O
    for j in range(3):
        countX=0
        countO=0
        for i in range(3):
            if a[i][j] == X:
                countX +=1
            if a[i][j] == O:
                countO +=1
        if countX==3:
            return X
        if countO==3:
            return O
    countX=0
    countO=0
    i=1
    j=1
    if a[i][j]==a[i-1][j-1] and a[i+1][j+1]==a[i][j]:
        if a[i][j]==X:
            return X
        if a[i][j]==O:
            return O
    if a[i][j]==a[i-1][j+1] and a[i+1][j-1]==a[i][j]:
        if a[i][j]==X:
            return X
        if a[i][j]==O:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    flag=True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                flag=False
    return flag


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == False:
        raise Exception("this is not a terminal state")

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    action_set=actions(board)
    optimal_action=None
    if player(board)==X:
        v=-1000
        for action in action_set:
            if v<Minplayervalue(result(board,action)):
                v=Minplayervalue(result(board,action))
                optimal_action=action
        return optimal_action
    if player(board) ==O:
        v=1000
        for action in action_set:
            if v>Maxplayervalue(result(board,action)):
                v=Maxplayervalue(result(board,action))
                optimal_action=action
        return optimal_action

def Maxplayervalue(board):
    if terminal(board):
        return utility(board)
    v=-1000
    action_set=actions(board)
    for action in action_set:
        result_board=result(board,action)
        v=max(v,Minplayervalue(result_board))
    return v
def Minplayervalue(board):
    if terminal(board):
        return utility(board)
    v=1000
    action_set=actions(board)
    for action in action_set:
        result_board=result(board,action)
        v=min(v,Maxplayervalue(result_board))
    return v
