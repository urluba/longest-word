# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import logging
import string
import requests
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

    @staticmethod
    def is_in_dictionnary(word: list) -> bool:
        try:
            response = requests.get(f'https://wagon-dictionary.herokuapp.com/{word}').json()
            was_found = response.get('found', False)
        except Exception as exc:
            logging.exception(exc)
            return False

        logging.debug(
            '%s was %s found in dictionnary',
            word,
            ' ' if was_found else 'not '
        )

        return was_found

    def is_valid(self, word: list) -> bool:
        if not Game.is_in_dictionnary(word):
            return False

        grid = copy(self.grid)

        for letter in word:
            logging.debug('Looking for %s in %s', letter, grid)
            if letter in grid:
                grid.remove(letter)
                continue

            return False

        return True
