
class Game:

    def __init__(self, map):
        self.map = map

    @staticmethod
    def generate_cell_neighbors(cell):
        neighbs = []
        neighbs.append((cell[0] + 1, cell[1] + 1))
        neighbs.append((cell[0] + 1, cell[1]))
        neighbs.append((cell[0] + 1, cell[1] - 1))
        neighbs.append((cell[0], cell[1] + 1))
        neighbs.append((cell[0], cell[1] - 1))
        neighbs.append((cell[0] - 1, cell[1] + 1))
        neighbs.append((cell[0] - 1, cell[1]))
        neighbs.append((cell[0] - 1, cell[1] - 1))

        return neighbs
