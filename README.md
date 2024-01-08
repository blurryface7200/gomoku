# AI-Gomoku-Player
 AI player for the Gomoku Board Game

![image](https://github.com/blurryface7200/gomoku/assets/94574451/0e32f8f1-2c28-499b-abca-025746711653)


Developed an AI in Python for the Gomoku Tournament, focusing on the classic board game Gomoku. The game follows the "free-style Gomoku" rules with an 11x11 board, where the first player to achieve five or more stones in a line (including diagonal lines) wins. Special rules like Swap, three-and-three, or four-and-four are not applicable.

The AI makes its move based on the result of the minimax function. It aims for the best move by maximizing its own score while minimizing the potential score of its opponent, effectively trying to force a win while preventing the opponent from winning. If the minimax function fails to find a move (which can happen if the depth limit 
is reached), the AI makes a random legal move.

GomokuAgentRand : is a very unintelligent computer player that only makes random, although legal, moves.

AI_Agent: is the intelligent AI player that uses minimax function.


TO RUN THE GAME: python gomoku.py PLAYER1 PLAYER2 
(where PLAYER1 & PLAYER2 are the AI player directories).

Example: python gomoku.py GomokuAgentRand AI_Agent1


https://github.com/blurryface7200/gomoku/assets/94574451/9b540392-d04f-4431-a3b9-16f40c2d8d20


