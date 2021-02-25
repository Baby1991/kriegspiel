from ..game import Game
from ..player import Player

import typing

class Command:
    name = 'ERROR'

    def __init__(self, args: list):
        self.args = args
        pass

    def start(self, player: Player, game: Game):
        pass

    def __str__(self):
        return '{0} {1}'.format(self.name, ' '.join(self.args))
