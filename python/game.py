from board import Board, Tiles
from player import Player

class Game:
    def __init__(self, args):
        self.board = Board(args["worldSeed"])

        self.players = [
            Player(
                args["playerSeed"], args["agents"],
                args["genotypeLength"],
                args["player1"]["breeding"],
                args["player1"]["selection"],
                args["player1"]["mutations"],
                self.board,
                args["player1"]["fitness"]
            ), 
            Player(
                args["playerSeed"],
                args["agents"],
                args["genotypeLength"],
                args["player2"]["breeding"],
                args["player2"]["selection"],
                args["player2"]["mutations"],
                self.board,
                args["player2"]["fitness"]
            )
        ]

        self.simulation = [ [], [] ]


    def run(self):
        winner = False
        for i in range(50):
            for j in range(2):
                winner = self.players[j].win
                self.simulation[j].append(self.players[j].createGeneration())
            if winner: break