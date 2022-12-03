from app.main import World


def test_app():
    x = 3
    y = 2
    world = World(x, y)
    world.create()

    assert world.x_max == x
    assert world.y_max == y

    traveller = world.tiles[0, 0].traveller_spone()

    assert traveller in world.tiles[0, 0].travellers
    assert traveller not in world.tiles[1, 2].travellers

    world.tiles[0, 0].traveller_leave(traveller)
    world.tiles[1, 2].traveller_come(traveller)

    assert traveller not in world.tiles[0, 0].travellers
    assert traveller in world.tiles[1, 2].travellers
