from .command import Command
from .error import ErrorCommand
from .join import JoinCommand
from .move import MoveCommand

import typing

def parse(command: str, game: Game):
    spl = command.split(' ')
    cmd = spl[0].lower()
    args = spl[1:]
    if cmd == 'join':
        return JoinCommand(args, game)
    elif cmd == 'move':
        return MoveCommand(args, game)
    else:
        return ErrorCommand(args, game)
