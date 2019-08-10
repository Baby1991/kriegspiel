from threading import Thread

import commands

class Player(Thread):
    def __init__(self, connection: socket, address, game: Game):
        super.__init__(self)
        self.address = address
        self.connection = connection
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
        # command

    def join(self):
        super.join(self)
        self.connection.close()
