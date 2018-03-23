import unittest

from game import Game


class TestGameOfLife(unittest.TestCase):

    def test_generate_neighbours(self):
        map = set()
        game = Game(map)

        cell_coordinates = (0,0)
        neighbors = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]

        self.assertItemsEqual(game.generate_cell_neighbors(cell_coordinates), neighbors)

    def test_update_map_with_neighbours(self):
        map = set()
        cell_coord = (0,0)
        map.add(cell_coord)
        game = Game(map)

        game.update_map()

        neighbors = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]
        new_map = neighbors.append(cell_coord)

        self.assertItemsEqual(game.map, new_map)


if __name__ == '__main__':
    unittest.main()