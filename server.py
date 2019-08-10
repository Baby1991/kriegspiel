from .game import Game
from threading import Thread

import commands
import events
import socket
import sys

PORT = len(sys.argv) > 1 and sys.argv[1] or 65432
game = Game()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', PORT))
    sock.listen()
    while True:
        try:
            conn, addr = sock.accept()
            with conn:
                game.connection(conn, addr)
        except KeyboardInterrupt:
            print('\u001B[1KExiting...')
            game.server_close()
            sock.close()
            break
