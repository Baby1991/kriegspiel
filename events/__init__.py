from .busy import BusyEvent
from .error import ErrorEvent
from .event import Event
from .invalid import InvalidEvent
from .move import MoveEvent
from .queue import QueueEvent
from .result import ResultEvent
from .start import StartEvent

import typing

def parse(event: str, game: Game) -> Event:
    spl = event.split(' ')
    evt = spl[0].lower()
    args = spl[1:]
    if evt == 'busy':
        return BusyEvent(args, game)
    elif evt == 'error':
        return ErrorEvent(args, game)
    elif evt == 'invalid':
        return InvalidEvent(args, game)
    elif evt == 'move':
        return MoveEvent(args, game)
    elif evt == 'queue':
        return QueueEvent(args, game)
    elif evt == 'result':
        return ResultEvent(args, game)
    elif evt == 'start':
        return StartEvent(args, game)
    else:
        return ErrorEvent(['no-event'], game)
