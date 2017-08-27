import random
from arrow import Arrow
from board import Board

class Player:

    def __init__(self, seed, amount, genotypeSize, breedFunction, selectionFunction, mutationFunction, board, weights):
        random.seed(seed)
        self.amount = amount
        self.arrows = []
        self.genotypeSize = genotypeSize
        self.weights = [weights["distance"], weights["pathLength"], weights["flatAngle"]]
        self.board = board
        self.createArrows()

        self.breedFunction = breedFunction
        self.selectionFunction = selectionFunction
        self.mutationFunction = mutationFunction
        self.breedArgs = []
        self.selectionArgs = []
        self.mutationArgs = []
        self.win = False
        
    def createArrows(self):
        for i in range(self.amount):
            self.arrows.append(Arrow(Arrow.randomGenotype(self.genotypeSize), self.board))

    def setBreedArgs(self,args):
        self.breedArgs = args

    def setSelectionArgs(self,args):
        self.selectionArgs = args

    def setMutationArgs(self,args):
        self.mutationArgs = args

    #returns list of genotypes
    def createGeneration(self):
        genotypes = self.moveArrows()
        selectedPairs = self.selectionFunction(self.arrows,self.weights, self.selectionArgs)
        breeded = self.breedFunction(selectedPairs, self.board, self.breedArgs)[:len(self.arrows)]
        nextGen = self.mutationFunction(breeded, self.board,self.mutationArgs)
        self.arrows = nextGen
        return genotypes

    def moveArrows(self):
        for a in self.arrows:
            a.move()
            if(a.win):
                self.win = True
        best = sorted(self.arrows,key=lambda arrow: arrow.fitness(self.weights),reverse=True)[:10]
        genotypeGeneration = []
        for g in best:
            genotypeGeneration.append(g.genotype)
        return genotypeGeneration

    @staticmethod
    def mutationRandom(breeded, board ,args):
        mutated = []
        for a in breeded:   
            for i in range(args["times"] if "times" in args else 1):
                genIndex = random.randint(1,len(a.genotype) - 1)
                newGen = random.randint(0,2)
                nextGenotype = a.genotype
                nextGenotype[genIndex] = newGen
            mutated.append(Arrow(nextGenotype, board))
        return mutated
        

    @staticmethod
    def breedMultiPoint(selectedPairs ,board, args):
        n = args["points"] if "points" in args else 1
        breeds = []
        points = []
        for i in selectedPairs:
            result1 = []
            result2 = []
            points = random.sample(range(1,len(i[0].genotype)-1), n)
            points.sort()
            last = 0
            for j in range(n):
                result1 += i[j%2].genotype[last:points[j]]
                result2 += i[(j+1)%2].genotype[last:points[j]]
                
                last = points[j]
            result1 += i[(n)%2].genotype[last:]
            result2 += i[(n+1)%2].genotype[last:]
            breeds.append(Arrow(result1, board))
            breeds.append(Arrow(result2, board))
        return breeds
    
    #returns pair of objects to be breed
    @staticmethod
    def selectionTournament(arrows, weights, args):
        sortedArrows = sorted(arrows,key=lambda arrow: arrow.fitness(weights),reverse=True)[:args["amount"] if "amount" in args else 2]
        selectedPairs = []
        for i in range(len(arrows)//2 + 1):
            posI = random.randint(0,len(sortedArrows)-1 )
            posJ = random.randint(0,len(sortedArrows)-1 )
            selectedPairs.append([sortedArrows[posI],sortedArrows[posJ]])

        selectedPairs[0] = [sortedArrows[0],sortedArrows[0]]
        selectedPairs[1] = [sortedArrows[1],sortedArrows[1]]
        return selectedPairs

    
def main():
    board = Board(5336)
    board.toString()
    player = Player(5336,10,30,Player.breedMultiPoint,Player.selectionTournamet,Player.mutationRandom,board,[0.2,0.3,0.5,0.4])
    print("\n".join([str(i) for i in player.createGeneration()]))


# def test():
#     board = Board(5336)
#     a = Arrow([6,2,1,0,2,1,2,0,1,2],board)
#     b = Arrow([4,2,1,0,1,1,2,1,0,1], board)
#     print([len(a.genotype) for a in Player.breedMultiPoint([[a,b],[b,a],[a,a],[b,b],[a,a]],board,{})])
    
# test()