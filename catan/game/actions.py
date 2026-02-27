from catan.game.game_state import GameState, Phases, ResourceMap
from catan.board.coordinates import CubeCoord, EdgeID, VertexID
from typing import Protocol, runtime_checkable
from dataclasses import dataclass

@runtime_checkable
class Action(Protocol):
    player_id: int
    def description(self) -> str:
        ...

    def is_valid(self, state: GameState) -> bool: 
        ...

@dataclass(frozen=True)
class RollDice():
    player_id: int

    def description(self) -> str:
        return f'Roll dice.'
    
    def is_valid(self, state: GameState) -> bool:
        return (
            state.current_player == self.player_id and 
            state.phase == Phases.ROLL
        )
    
@dataclass(frozen=True)
class MoveRobber():
    player_id: int
    target: CubeCoord

    def description(self) -> str:
        return f'Move robber to {self.target} hex.'
    
    def is_valid(self, state: GameState) -> bool:
        return (
            state.current_player == self.player_id and 
            state.phase == Phases.ROBBER
        )

@dataclass(frozen=True)
class BuildRoad():
    player_id: int
    edge_id: EdgeID

    def description(self) -> str:
        return f'Build a road at: {self.edge_id}.'
    
    def is_valid(self, state: GameState) -> bool:
        # only a quick and cheap check
        return (
            state.current_player == self.player_id and 
            state.phase == Phases.BUILD_AND_TRADE and 
            state.resources[self.player_id].can_afford(ResourceMap(brick = 1, wood = 1))
        )

@dataclass(frozen=True)
class BuildSettlement():
    player_id: int
    vertex_id: VertexID

    def description(self) -> str:
        return f'Build a settlement at: {self.vertex_id}.'
    
    def is_valid(self, state: GameState) -> bool:
        return (
            state.current_player == self.player_id and 
            state.phase == Phases.BUILD_AND_TRADE and
            state.resources[self.player_id].can_afford(ResourceMap(brick = 1, wood = 1, wool = 1, grain = 1))
        )
    
@dataclass(frozen=True)
class BuildCity():
    player_id: int
    vertex_id: VertexID

    def description(self) -> str:
        return f'Build a city at: {self.vertex_id}.'
    
    def is_valid(self, state: GameState) -> bool:
        return (
            state.current_player == self.player_id and 
            state.phase == Phases.BUILD_AND_TRADE and
            state.resources[self.player_id].can_afford(ResourceMap(grain = 2, ore = 3))
        )
    
@dataclass(frozen=True)
class BuyDevCard():
    player_id: int

    def description(self) -> str:
        return f'Buy a development card.'
    
    def is_valid(self, state: GameState) -> bool:
        return (
            state.current_player == self.player_id and 
            state.phase == Phases.BUILD_AND_TRADE and
            state.resources[self.player_id].can_afford(ResourceMap(wool = 1, grain = 1, ore = 1))
        )

@dataclass(frozen=True)
class Trade():
    player_id: int
    offer_give: ResourceMap
    offer_want: ResourceMap

    def description(self) -> str:
        return f'Offer to trade {self.offer_give} for {self.offer_want}'
    
    def is_valid(self, state: GameState) -> bool:
        return (
            state.current_player == self.player_id and 
            state.phase == Phases.BUILD_AND_TRADE and
            state.resources[self.player_id].can_afford(self.offer_give)
        )
    
@dataclass(frozen=True)
class EndTurn():
    player_id: int

    def description(self) -> str:
        return f'End turn.'
    
    def is_valid(self, state: GameState) -> bool:
        return state.current_player == self.player_id