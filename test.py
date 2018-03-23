import unittest

import Game from game


class TestGameOfLife(unittest.TestCase):

    def test_generate_neighbours(self):
        game = Game(map)

        cell_coordinates = (0,0)
        neighbors = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]

        self.assertItemsEqual(game.generate_cell_neighbors(cell_coordinates), neighbors)


if __name__ == '__main__':
    unittest.main()