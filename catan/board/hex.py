from dataclasses import dataclass
from enum import Enum, auto

class Terrain(Enum):
    FOREST = auto()     # (Lumber)
    PASTURE = auto()    # (Wool)
    FIELDS = auto()     # (Grain)
    HILLS = auto()      # (Brick)
    MOUNTAINS = auto()  # (Ore)
    DESERT = auto()     # No resource

@dataclass(frozen = True)
class Hex:
    terrainType: Terrain
    numberToken: int | None

    def __post_init__(self):
        # validate init
        if self.terrainType == Terrain.DESERT and self.numberToken is not None:
            raise ValueError("Desert hex must have no number token")
        elif self.numberToken is not None:
            if not (2 <= self.numberToken <= 12) or self.numberToken == 7:
                raise ValueError("Invalid number token value. Must be [2-12] and != 7")
            
    @property
    def is_desert(self) -> bool:
        return self.terrainType == Terrain.DESERT