from catan.game.game_state import GameState, Phases
from catan.game.resources import ResourceMap
from catan.board.board_layout import STANDARD_BOARD
import pytest


class TestGameState:
    def test_invalid_new_game(self):
        with pytest.raises(ValueError):
            GameState.new_game(STANDARD_BOARD, -1)

    def test_invalid_player_count_high(self):
        with pytest.raises(ValueError):
            GameState.new_game(STANDARD_BOARD, 5)

    def test_invalid_current_player(self):
        with pytest.raises(ValueError):
            GameState(STANDARD_BOARD, 4, -1, {r: ResourceMap() for r in range(4)}, {p: 0 for p in range(4)}, Phases.SETUP)

    def test_valid_new_game(self):
        gs = GameState.new_game(STANDARD_BOARD, 2)
        assert gs.players == 2
        assert gs.current_player == 0
        assert gs.phase == Phases.SETUP

    def test_new_game_resources_empty(self):
        gs = GameState.new_game(STANDARD_BOARD, 4)
        for i in range(4):
            assert gs.resources[i] == ResourceMap()

    def test_new_game_vp_zero(self):
        gs = GameState.new_game(STANDARD_BOARD, 4)
        for i in range(4):
            assert gs.vp[i] == 0

    def test_clone_is_new_object(self):
        gs = GameState.new_game(STANDARD_BOARD, 2)
        gs_clone = gs.clone()
        assert gs_clone == gs
        assert gs_clone is not gs