from .command import Command
from ..events import ErrorEvent
from ..game import Game
from ..player import Player

import chess

class MoveCommand(Command):
    name = 'MOVE'

    def start(self, player: Player, game: Game):
        index = -1
        try:
            index = int(self.args) % len(player.legal_moves)
        except ValueError:
            player.event(ErrorEvent([]))
            return
        move = chess.Move.from_uci(game.board.legal_moves[index])
        if not game.board.is_legal(move):
            print('Something, somewhere, went terribly wrong:', game.board, move)
        game.board.push(move)
        game.board.pop()
        player.opponent().start_move()
