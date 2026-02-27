from catan.game.actions import *
import pytest

class TestActions:
    def test_is_instance(self):
        assert (
            isinstance(RollDice, Action) and
            isinstance(MoveRobber, Action) and
            isinstance(BuildRoad, Action) and
            isinstance(BuildSettlement, Action) and
            isinstance(BuildCity, Action) and
            isinstance(BuyDevCard, Action) and
            isinstance(Trade, Action) and
            isinstance(EndTurn, Action)
        )

    

'''
Returns False when it's not the current player's turn
Returns False when in wrong phase
Returns False when can't afford it
Returns True when all conditions met
'''