import sys, json
from game import Game

def main():
    #in
    args = json.load( sys.stdin )

    #run
    game = Game(args)
    game.run()
    
    #out
    print(json.dumps(
        {
            "board": {
                "obstacles":  game.board.obstacles,
                "start" : game.board.start,
                "end" : game.board.end,
            },
            "player1" : game.simulation[0],
            "player2" : game.simulation[1]
        }
    ))


main()