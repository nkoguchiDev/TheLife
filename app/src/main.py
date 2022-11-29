import numpy as np
import uuid


class Traveller:
    def __init__(self) -> None:
        self.life = 100


class Tile:
    def __init__(self) -> None:
        self.endurance = 10
        self.travellers = {}


class World:
    def __init__(self) -> None:
        self.w_map = None
        self.day = 0

    def create(self, x: int, y: int) -> None:
        w = []
        for _ in range(y):
            w_x = []
            for _ in range(x):
                w_x.append(Tile())
            w.append(w_x)
        self.w_map = np.array(w)

    def traveller_spone(self) -> str:
        _id = uuid.uuid4().hex
        self.w_map[0, 0].travellers[_id] = Traveller()
        return _id


if __name__ == "__main__":
    world = World()
    world.create(3, 2)
    world.traveller_spone()
    world.traveller_spone()
    print(world.w_map[0, 0].travellers)
