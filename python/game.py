from board import Board, Tiles
from player import Player

class Game:
    def __init__(self, args):
        self.board = Board(args["worldSeed"])

        #TODO MAKE BETTER FUNCTIONS
        functions = {
            "tournament" : Player.selectionTournament,
            "random" : Player.selectionTournament,
        }

        self.players = [
            Player(
                args["playerSeed"], 
                args["agents"],
                args["genotypeLength"],
                Player.breedMultiPoint,
                functions[args["player1"]["selection"]],
                Player.mutationRandom,
                self.board,
                args["player1"]["fitness"]
            ), 
            Player(
                args["playerSeed"],
                args["agents"],
                args["genotypeLength"],
                Player.breedMultiPoint,
                functions[args["player2"]["selection"]],
                Player.mutationRandom,
                self.board,
                args["player2"]["fitness"]
            )
        ]

        self.players[0].setBreedArgs({"points" : args["player1"]["breeding"]})
        self.players[1].setBreedArgs({"points" : args["player2"]["breeding"]})

        self.players[0].setMutationArgs({"times" : args["player1"]["mutations"]})
        self.players[1].setMutationArgs({"times" : args["player2"]["mutations"]})

        self.players[0].setSelectionArgs({"amount" : args["agents"]//2})
        self.players[1].setSelectionArgs({"amount" : args["agents"]//2})

        #TODO Selection args
        
        self.simulation = [ [], [] ]


    def run(self):
        winner = False
        for i in range(200):
            for j in range(2):
                winner = self.players[j].win
                self.simulation[j].append(self.players[j].createGeneration())
            if winner:
                print("gano")
                print(i)
                break