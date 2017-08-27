import sys, json

def main():
    #in
    args = json.load( sys.stdin )

    worldSeed = args["worldSeed"]
    playerSeed = args["playerSeed"]
    breeding = args["breeding"]
    selection = args["selection"]
    mutations = args["mutations"]
    fitness = args["fitness"]
    agents = args["agents"]
    genotypeLength = args["genotypeLength"]

    #run

    


    #out

    simulation = {
        "board": {
            "obstacles": [
                [3,3],
                [20,20]
            ],
            "start" : [50,50],
            "end" : [0,0],
        },
        "Player1" : [
            [
                [0,0,0,1,0,2,1,2,2],
                [0,1,2,1,2,0,1,2,3]
            ],
            [
                [0,0,0,1,0,2,1,2,2],
                [0,1,2,1,2,0,1,2,3]
            ]
        ],
        "Player2" :[                    #player
            [                               #generation
                [0,0,0,1,0,2,1,2,2],            #genome
                [0,1,2,1,2,0,1,2,3]
            ],
            [
                [0,0,0,1,0,2,1,2,2],
                [0,1,2,1,2,0,1,2,3]
            ]
        ]
    }

    print (json.dumps(simulation))


main()