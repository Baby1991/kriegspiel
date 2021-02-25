from events import Event, MoveEvent
from threading import Thread
from .game import Game

import commands
import socket

class Player(Thread):
    connection: socket = None
    def __init__(self, connection: socket, address, game: Game):
        super.__init__(self)
        self.address = address
        self.connection: socket = connection
        self.game = game

    def start(self):
        super.start(self)
        print('New socket:', self.address)
        while True:
            try:
                data = self.connection.recv(1024)
                if not data:
                    game.remove_player(self)
                    break
                self.command(data.decode('utf-8'))
            except OSError:
                game.remove_player(self)
                break

    def command(self, cmd):
        command = commands.parse(cmd)
        command.start(self, self.game)

    def join(self):
        super.join(self)
        self.connection.close()

    def event(self, event: Event):
        self.connection.send('%b' % event)

    def opponent(self):
        self.game.opponent_of(self)

    def start_move(self):
        self.connection.send('%b' % MoveEvent(self.game.board.legal_moves))
