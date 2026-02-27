from catan.board.board import Board
from catan.board.board_layout import STANDARD_BOARD
from catan.game.resources import ResourceMap
from enum import Enum, auto
from dataclasses import dataclass
import copy

class Phases(Enum):
    SETUP = 0
    ROLL = 1                # resource production
    BUILD_AND_TRADE = 2
    ROBBER = 3              # triggered by a 7 roll
    GAME_OVER = 4

@dataclass(frozen=True)
class GameState:
    board: Board
    players: int
    current_player: int
    resources: dict[int, ResourceMap]
    vp: dict[int, int]
    phase: Phases

    @classmethod
    def new_game(cls, board: Board, players: int) -> 'GameState':
        return cls(
            board = board,
            players = players,
            current_player = 0, 
            resources = {r: ResourceMap() for r in range(players)}, 
            vp = {p: 0 for p in range(players)},
            phase = Phases.SETUP
        )

    def __post_init__(self):
        if not (2 <= self.players <= 4):
            raise ValueError(f'# of players must be 2-4 inclusive, not: {self.players}')
        if not (0 <= self.current_player <= self.players - 1):
            raise ValueError(f'Invalid current player: {self.current_player}')
    
    def clone(self) -> 'GameState':
        return copy.deepcopy(self)