import unittest

from game import Game


class TestGameOfLife(unittest.TestCase):

    def test_generate_neighbours(self):
        map = set()
        game = Game(map)

        cell_coordinates = (0,0)
        neighbors = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]

        self.assertItemsEqual(game.generate_cell_neighbors(cell_coordinates), neighbors)


if __name__ == '__main__':
    unittest.main()