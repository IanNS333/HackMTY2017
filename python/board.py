import random

class Tiles:
    Space, Obstacle, Flag , Start = range(4)


class Board:
    def __init__(self, sd):
        self.board = []
        self.seed = sd

        self.obstacles = []
        self.start = []
        self.end = []
        

        random.seed(self.seed)

        self.iMax = 25
        self.jMax = 50

        self.lineObLower = 0.05
        self.lineObUpper = 0.1

        #create lines with rand obstacle and seed shuffle 
        for i in range(self.iMax):
            lineObst = random.randint(int(self.jMax*self.lineObLower), int(self.jMax*self.lineObUpper))

            line = []

            for j in range(lineObst):          line.append(Tiles.Obstacle)
            for j in range(self.jMax - lineObst):   line.append(Tiles.Space)

            random.shuffle(line)

            self.board.append(line)

        random.shuffle(self.board)     

        # extract obstacles
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == Tiles.Obstacle:
                    self.obstacles.append([i, j])


        #place flag
        flagI = random.randint(0, (self.iMax)-1)
        flagJ = random.randint(self.jMax - int(self.jMax*0.2), self.jMax-1)

        self.end = [flagI, flagJ]
        self.board[flagI][flagJ] = Tiles.Flag

        # place start
        startI = random.randint(0, (self.iMax)-1)
        startJ = random.randint(0 , int(0.2*self.jMax-1))

        self.start = [startI, startJ]
        self.board[startI][startJ] = Tiles.Start


    def at(self, position):
        i = position[0]
        j = position[1]
        if(i < 0 or i >= self.iMax or j < 0 or j >= self.jMax):
            return Tiles.Obstacle
        return self.board[i][j]

    def debug_print(self):
        trans = {
            Tiles.Space : " ",
            Tiles.Obstacle : "#",
            Tiles.Flag : "F",
            Tiles.Start :  "S"
        }
        for line in self.board:
            print(" ".join([trans[i] for i in line]))

    def toString(self):
        for line in self.board: 
            print(line)
        print (self.start)
        print (self.end)
