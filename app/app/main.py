import numpy as np
import uuid


class Traveller:
    def __init__(self, id: str) -> None:
        self.id = id
        self.life = 100
        self.motivation = 100
        self.emotion = {}


class Tile:
    def __init__(self) -> None:
        self.endurance = 10
        self.travellers = []

    def traveller_leave(self, traveller: Traveller) -> None:
        self.travellers.remove(traveller)

    def traveller_come(self, traveller: Traveller) -> None:
        self.travellers.append(traveller)

    def traveller_spone(self) -> str:
        traveller = Traveller(uuid.uuid4().hex)
        self.traveller_come(traveller)
        return traveller


class World:
    def __init__(self, x, y) -> None:
        self.tiles = None
        self.day = 0
        self.x_max = x
        self.y_max = y

    def create(self) -> None:
        w = []
        for _ in range(self.y_max):
            x = []
            for _ in range(self.x_max):
                x.append(Tile())
            w.append(x)
        self.tiles = np.array(w)


if __name__ == "__main__":
    pass
