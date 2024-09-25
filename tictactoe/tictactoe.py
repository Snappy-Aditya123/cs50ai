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
    Returns the player whose turn it is on a given board.
    """
    # Count the number of X's and O's
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    # X always goes first, so if they have more, it's O's turn, otherwise it's X's
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()  # Use set to avoid duplicates
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                action.add((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")

    # Make a deep copy of the board to avoid mutating the original
    modified_board = copy.deepcopy(board)
    modified_board[action[0]][action[1]] = player(board)
    return modified_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row == [X, X, X]:
            return X
        if row == [O, O, O]:
            return O
    
    # Check columns
    for j in range(3):
        if [board[i][j] for i in range(3)] == [X, X, X]:
            return X
        if [board[i][j] for i in range(3)] == [O, O, O]:
            return O
    
    # Check diagonals
    if [board[i][i] for i in range(3)] == [X, X, X] or [board[i][2-i] for i in range(3)] == [X, X, X]:
        return X
    if [board[i][i] for i in range(3)] == [O, O, O] or [board[i][2-i] for i in range(3)] == [O, O, O]:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there's a winner, game is over
    if winner(board) is not None:
        return True
    
    # If no empty cells remain, game is over (it's a tie)
    return all(cell is not EMPTY for row in board for cell in row)

 
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0
'''
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    possible_actions = actions(board)
    current_player = player(board)  
    boards = [result(board,act) for act in possible_actions]
    all_scores = []
    for bo in board:
        pass
'''    
    
 
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    possible_actions = actions(board)
    current_player = player(board)
    
    if current_player == X:
        print('Xs turn')
        # Maximizing for X
        best_score = -math.inf
        best_action = None
        
        for action in possible_actions:
            new_board = result(board, action)
            score = min_max_mini(new_board, False)  # False means it's now O's turn (minimizing)
            if score > best_score:
                best_score = score
                best_action = action
            print(best_score)
    else:    
    
        print('Os turn')
    # Minimizing for O
        best_score = math.inf
        best_action = None
        for action in possible_actions:
            new_board = result(board, action)
            score = min_max_mini(new_board, True)  # True means it's now X's turn (maximizing)
            print(score)
            if score < best_score:
                best_score = score
                best_action = action
            
    return best_action


def min_max_mini(board, is_maximizing):
    """
    Recursively evaluates the board and returns the optimal score.
    is_maximizing: True if it's X's turn (maximize score), False if it's O's turn (minimize score).
    """
    if terminal(board):
        return utility(board)
    
    possible_actions = actions(board)
    
    if is_maximizing:
        best_score = -math.inf
        for action in possible_actions:
            new_board = result(board, action)
            score = min_max_mini(new_board, False)  # O's turn after X
            
            best_score = max(best_score, score)
        return best_score
    
    else:
        best_score = math.inf
        for action in possible_actions:
            new_board = result(board, action)
            score = min_max_mini(new_board, True)  # X's turn after O
            
            best_score = min(best_score, score)
        return best_score


def hamscore(board):
    pass
