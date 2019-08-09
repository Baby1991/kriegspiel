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
    if evt == 'BUSY':
        return BusyEvent(args)
