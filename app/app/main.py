import numpy as np


class Traveller:
    def __init__(self, x, y) -> None:
        self.life = 100
        self.motivation = 100
        self.emotion = {}
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


class Tile:
    def __init__(self) -> None:
        self.durability = 10


class World:
    def __init__(self, x, y) -> None:
        self.tiles = None
        self.day = 0

        matrix = []
        for _ in range(y):
            row = []
            for _ in range(x):
                row.append(Tile())
            matrix.append(row)
        self.tiles = np.array(matrix)

        self.traveller = Traveller(0, 0)

    @property
    def x_len(self):
        return self.tiles.shape[1]

    @property
    def y_len(self):
        return self.tiles.shape[0]


if __name__ == "__main__":
    pass
