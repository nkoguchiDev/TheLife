from app.main import World


def test_app():
    x = 3
    y = 2
    world = World(x, y)

    assert world.x_len == x
    assert world.y_len == y

    assert world.tiles[
        world.traveller.x,
        world.traveller.y
    ].durability == 10
