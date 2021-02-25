from .busy import BusyEvent
from .error import ErrorEvent
from .event import Event
from .invalid import InvalidEvent
from .move import MoveEvent
from .queue import QueueEvent
from .result import ResultEvent
from .start import StartEvent

import typing

def parse(event: str) -> Event:
    spl = event.split(' ')
    evt = spl[0].lower()
    args = spl[1:]
    if evt == 'busy':
        return BusyEvent(args)
    elif evt == 'error':
        return ErrorEvent(args)
    elif evt == 'invalid':
        return InvalidEvent(args)
    elif evt == 'move':
        return MoveEvent(args)
    elif evt == 'queue':
        return QueueEvent(args)
    elif evt == 'result':
        return ResultEvent(args)
    elif evt == 'start':
        return StartEvent(args)
    else:
        return ErrorEvent(['no-event'])
