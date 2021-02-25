from .command import Command
from ..events import ErrorEvent
from ..game import Game

class ErrorCommand(Command):
    def start(self, player: Player, game: Game):
        player.event(ErrorEvent(['no-command']))
