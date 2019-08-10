from .player import Player

import chess
import typing

class Game:
    board: chess.Board = chess.Board()
    players = []

    def connection(self, conn, addr):
        new_player = Player(conn, addr, self)
        players.append(new_player)
        new_player.start()

    def remove_player(self, player: Player):
        players.remove(player)
        player.join()

    def server_close(self):
        for player in players:
            player.join()
