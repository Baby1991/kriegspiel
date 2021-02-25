from .command import Command
from .error import ErrorCommand
from .join import JoinCommand
from .move import MoveCommand

import typing

def parse(command: str):
    spl = command.split(' ')
    cmd = spl[0].lower()
    args = spl[1:]
    if cmd == 'join':
        return JoinCommand(args)
    elif cmd == 'move':
        return MoveCommand(args)
    else:
        return ErrorCommand(args)
