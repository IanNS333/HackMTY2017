import random, math
from board import Tiles, Board

class Arrow:
    
    #self, genotype (array of ints)
    def __init__(self, genotype, board):
        self.genotype = genotype
        self.direction = self.genotype[0]
        self.timeAlive = 1
        self.board = board
        self.position = start

    #int (number of steps)
    def getTimeAlive(self):
        return self.timeAlive

    #string
    def getGenotype(self):
        return self.genotype

    #float (not normalized)
    def fitness(self, weights):
        res = 0
        res += weights[0]*self.euclideanFit(self.board.flag)
        return res

    def move(self):
        alive = true
        while(alive):
            nextGen = self.genotype[timeAlive]
            nextDirection = direction + genotype - 1
            nextPosition = moveTo(nextDirection, self.position)
            if (self.board.at(nextPosition) == Tiles.Obstacle or self.board.at(nextPosition) == Tiles.Flag):
                alive = False
            self.direction = nextDirection

                
    def moveTo()

    #returns array of 0s, 1s and 2s, first element declares degree which is from 0 to 7
    @staticmethod
    def randomGenotype(randint, length):
        genotype = []
        genotype.append(randint(0,7))
        for i in range(length):
            genotype.append(randint(0,2))
        return genotype

    def euclideanFit(self,flag):
        return 1/math.sqrt((flag[0] - self.position[0])** + (flag[1] - self.position[1])**)