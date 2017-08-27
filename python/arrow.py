import random, math
from board import Tiles, Board

class Arrow:
    
    #self, genotype (array of ints)
    def __init__(self, genotype, board):
        self.genotype = genotype
        self.direction = self.genotype[0]
        self.timeAlive = 1
        self.board = board
        self.position = board.start
        self.win = False

    #float (not normalized)
    def fitness(self, weights):
        res = 0
        res += weights[0]*self.euclideanFit(self.board.end)
        return res

    def move(self):
        alive = True
        positions = []
        while(alive and self.timeAlive < len(self.genotype)):
            positions.append(self.position)
            nextGen = self.genotype[self.timeAlive]
            nextDirection = self.direction + nextGen
            nextPosition = self.moveTo(nextDirection, self.position)
            if(nextDirection%2 == 1 and (self.board.at(self.moveTo(nextDirection-1, self.position)) == Tiles.Obstacle or self.board.at(self.moveTo(nextDirection+1, self.position)) == Tiles.Obstacle)):
                alive = False
                self.win = True
            elif (self.board.at(nextPosition) == Tiles.Obstacle or self.board.at(nextPosition) == Tiles.Flag):
                alive = False
            self.direction = nextDirection
            self.position = nextPosition
            self.timeAlive+=1
        print(positions)

    
    def moveTo(self,direction, position):
        direction %= 8
        if(direction == 0):
            return [position[0],position[1]+1]
        elif (direction == 1):
            return [position[0]+1,position[1]+1]
        elif (direction == 2):
            return [position[0]+1,position[1]]
        elif (direction == 3):
            return [position[0]+1,position[1]-1]
        elif (direction == 4):
            return [position[0],position[1]-1]
        elif (direction == 5):
            return [position[0]-1,position[1]-1]
        elif (direction == 6):
            return [position[0]-1,position[1]]
        elif (direction == 7):
            return [position[0]-1,position[1]+1]
        

    #returns array of 0s, 1s and 2s, first element declares degree which is from 0 to 7
    @staticmethod
    def randomGenotype(length):
        genotype = []
        genotype.append(random.randint(0,7))
        for i in range(length):
            genotype.append(random.randint(0,2))
        return genotype

    def euclideanFit(self,flag):
        return 1/math.sqrt((flag[0] - self.position[0])**2 + (flag[1] - self.position[1])**2)

