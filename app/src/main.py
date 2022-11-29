import numpy as np
import uuid


class Traveller:
    def __init__(self) -> None:
        self.life = 100


class Tile:
    def __init__(self) -> None:
        self.endurance = 10
        self.travellers = {}

    def traveller_leave(self, id: str) -> Traveller:
        traveller = self.travellers[id]
        del self.travellers[id]
        return traveller

    def traveller_come(self, id: str, traveller: Traveller) -> None:
        self.travellers[id] = traveller

    def traveller_spone(self) -> str:
        _id = uuid.uuid4().hex
        self.travellers[_id] = Traveller()
        return _id


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


if __name__ == "__main__":
    world = World()
    world.create(3, 2)
    _id = world.w_map[0, 0].traveller_spone()
    print(world.w_map[0, 0].travellers)
    print(world.w_map[1, 2].travellers)

    traveller = world.w_map[0, 0].traveller_leave(_id)
    world.w_map[1, 2].traveller_come(_id, traveller)

    print(world.w_map[0, 0].travellers)
    print(world.w_map[1, 2].travellers)
