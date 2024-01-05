##################################################
# Student No : 2042274
# CSC325 Coursework 2
# AI for the CSC325 Gomoku Tournament
##################################################




import numpy as np
from misc import legalMove, winningTest
from gomokuAgent import GomokuAgent

class Player(GomokuAgent):
    def __init__(self, ID, BOARD_SIZE, X_IN_A_LINE, search_depth=3):
        super().__init__(ID, BOARD_SIZE, X_IN_A_LINE)
        self.search_depth = search_depth
        self.opponent_ID = -1 * ID 


    # This method calls the minimax function to get the best move for the current board state
    #If the minimax function returns None for the best move (which can happen if the depth limit 
    # is reached and no winning or losing move is found), it falls back to a random legal move.
    def move(self, board):
        best_score, best_move = self.minimax(board, self.search_depth, self.ID, float('-inf'), float('inf'))
        if best_move is None:
            # Fallback to a random legal move if the minimax function returns None
            legal_moves = self.generate_legal_moves(board)
            best_move = legal_moves[np.random.randint(len(legal_moves))]
        
        return best_move
    

    #This method uses the Minimax algorithm with Alpha-Beta pruning to search the game tree and 
    # find the best move. It recursively explores all possible moves up to a certain depth, 
    # simulating alternating turns between the AI and its opponent. The recursion stops when it 
    # reaches the maximum depth or a winning move for either player. The function then returns 
    # the score of the board configuration and the best move.
    def minimax(self, board, depth, player, alpha, beta):
        # Base cases for the minimax recursion
        # If the depth limit has been reached or if any player has won, evaluate the board state and return the score
        if depth == 0 or winningTest(self.ID, board, self.X_IN_A_LINE) or winningTest(self.opponent_ID, board, self.X_IN_A_LINE):
            return self.evaluate(board), None

        legal_moves = self.generate_legal_moves(board)

        # Player's turn (maximizing player)
        if player == self.ID:
            max_score = float('-inf')
            best_move = None 
            for move in legal_moves:
                new_board = board.copy()
                new_board[move] = player
                score, _ = self.minimax(new_board, depth - 1, self.opponent_ID, alpha, beta)# Recursively call minimax for the new board state
                if score > max_score:
                    max_score = score
                    best_move = move
                alpha = max(alpha, max_score)
                if beta <= alpha: # If beta is less than or equal to alpha, break the loop (Alpha-Beta pruning)
                    break
            return max_score, best_move if best_move is not None else legal_moves[0]
        
        # Opponent's turn (minimizing player)
        else:
            min_score = float('inf')
            best_move = None
            for move in legal_moves:
                new_board = board.copy()
                new_board[move] = player
                score, _ = self.minimax(new_board, depth - 1, self.ID, alpha, beta)# Recursively call minimax for the new board state
                if score < min_score:
                    min_score = score
                    best_move = move
                beta = min(beta, min_score)
                if beta <= alpha:# If beta is less than or equal to alpha, break the loop (Alpha-Beta pruning)
                    break
            return min_score, best_move

    # This function evaluates the current board state.
    # If the player has won, return positive infinity.
    # If the opponent has won, return negative infinity.
    # Otherwise, return 0.
    def evaluate(self, board):
        if winningTest(self.ID, board, self.X_IN_A_LINE):
            return float('inf')
        elif winningTest(self.opponent_ID, board, self.X_IN_A_LINE):
            return float('-inf')
        else:
            return 0

    # This function generates all legal moves for the current board state.
    def generate_legal_moves(self, board):
        legal_moves = []
        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                if board[r, c] == 0:
                    legal_moves.append((r, c))
        return legal_moves
    

#The AI makes its move based on the result of the minimax function. It aims to maximize its own 
# score while minimizing the potential score of its opponent, effectively trying to force a win 
# while preventing the opponent from winning. If the minimax function fails to find a move, the 
# AI makes a random legal move.
