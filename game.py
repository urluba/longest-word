# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import logging
import string
from copy import copy
from random import choice

logging.basicConfig(level=logging.DEBUG)

class Game:
    grid_size = 9

    @staticmethod
    def _generate_grid(size: int) -> list:
        new_grid = list()
        for _ in range(size):
            new_grid.append(
                choice([i for i in string.ascii_uppercase])
            )

        logging.debug('Grid was generated as "%s"', new_grid)
        return new_grid

    def __init__(self, grid_size: int = None):
        if grid_size:
            self.grid_size = grid_size

        self.grid = Game._generate_grid(Game.grid_size)

    def is_valid(self, word: list) -> bool:
        grid = copy(self.grid)

        for letter in word:
            logging.debug('Looking for %s in %s', letter, grid)
            if letter in grid:
                grid.remove(letter)
                continue

            return False

        return True
