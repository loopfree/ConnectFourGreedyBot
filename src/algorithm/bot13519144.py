from src.model import State
import random

class Bot13519144:
    def init(self) -> None:
        pass

    def find(self, state: State, player: int, thinking_time: float) -> int:
        """
        [DESC]
            Function to find the best move for player
        [PARAMS]
            state: State -> current state
            player: int -> player to find the best move
            thinking_time: float -> time limit for bot to find the best move
        [RETURN]
            int -> column to place piece
        """
        # Implement greedy algorithm here
        # ...

        return random.randint(0, state.board.col)