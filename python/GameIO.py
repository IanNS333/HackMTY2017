import sys, json

def main():
    request = json.load( sys.stdin )
    worldSeed = request["worldSeed"]
    playerSeed = request["playerSeed"]
    param1 = request["param1"]
    param2 = request["param2"]
    agents = request["agents"]

    print(worldSeed)
    
    for i in ["a","b","c"]:
        print(param1[i] if i in param1 else -1)
        print(param2[i] if i in param2 else -1)

main()