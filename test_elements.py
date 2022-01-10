from elements import Tile, Barrel, Spot


def test_creat_tile():
    tile = Tile((1, 1))
    assert tile


def test_tile_position():
    tile = Tile((1, 1))
    assert tile.rect.topleft == (1, 1)


def test_creat_barrel():
    barrel = Barrel((1, 1))
    assert barrel


def test_barrel_position():
    barrel = Barrel((1, 1))
    assert barrel.rect.topleft == (1, 1)


def test_creat_spot():
    spot = Spot((1, 1))
    assert spot


def test_spot_position():
    spot = Spot((1, 1))
    assert spot.rect.topleft == (1, 1)
