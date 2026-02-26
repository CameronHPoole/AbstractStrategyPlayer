from catan.board.hex import Hex, Terrain
import pytest

class TestHex:
    def test_desert_none_token(self):
        with pytest.raises(ValueError):
            h = Hex(Terrain.DESERT, 6)

    def test_hex_under_2(self):
        with pytest.raises(ValueError):
            h = Hex(Terrain.FIELDS, 1)

    def test_hex_equals_7(self):
        with pytest.raises(ValueError):
            h = Hex(Terrain.FIELDS, 7)
        
    def test_hex_above_12(self):
        with pytest.raises(ValueError):
            h = Hex(Terrain.FIELDS, 13)

    def test_hex_correct(self):
        h = Hex(Terrain.MOUNTAINS, 8)
        assert not h.is_desert
        assert h.terrainType == Terrain.MOUNTAINS
        assert h.numberToken == 8

    def test_desert_is_desert(self):
        h = Hex(Terrain.DESERT, None)
        assert h.is_desert