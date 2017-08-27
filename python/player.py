import random
from arrow import Arrow

class Player:

    def __init__(self, seed, amount, genotypeSize, breedFunction, selectionFunction, mutationFunction, game, weights):
        random.seed(seed)
        self.amount = amount
        self.arrows = []
        self.genotypeSize = genotypeSize
        self.weights = weights
        self.game = game
        self.createArrows()

        self.breedFunction = breedFunction
        self.selectionFunction = selectionFunction
        self.mutationFunction = mutationFunction
        self.breedArgs = []
        self.selectionArgs = []
        self.mutationArgs = []
        
    def createArrows(self):
        for i in range(self.amount):
            self.arrows.append(Arrow(Arrow.randomGenotype(random,self.genotypeSize), self.game.board))

    def setBreedArgs(self,args):
        self.breedArgs = args

    def setSelectionArgs(self,args):
        self.selectionArgs = args

    def setMutationArgs(self,args):
        self.mutationArgs = args

    #returns list of genotypes
    def createGeneration(self):
        genotypes = self.moveArrows()
        selectedPairs = self.selectionFunction(self.arrows, self.selectionArgs)
        breeded = self.breedFunction(selectedPairs, self.breedArgs)
        nextGen = self.mutationFunction(breeded, random.randint,self.mutationArgs)
        self.arrows = nextGen
        return genotypes

    def moveArrows(self):
        generationGenotypes = []
        for a in self.arrows:
            generationGenotypes.append(a.getGenotype())
            a.move()
        return generationGenotypes

    @staticmethod
    def mutationRandom(breeded, board ,args):
        mutated = []
        for a in breeded:    
            for i in range(args["times"] if "times" in args else 1):
                genIndex = random.randint(1,len(a.genotype) - 1)
                newGen = random.randint(0,2)
                mutated.append(Arrow(a.genotype, board))
        

    @staticmethod
    def breedMultiPoint(selectedPairs ,board, args):
        n = args["points"] if "points" in args else 1
        breeds = []
        for i in selectedPairs:
            point = random.randint(1, len(selectedPairs[0].genotype)-1)
            breeds.append(Arrow(i[0].genotype[:point] + i[1].genotype[point:-1], board))
        return breeds
    
    #returns pair of objects to be breed
    @staticmethod
    def selectionTournamet(arrows, args):
        sortedArrows = sorted(arrows,key=lambda arrow: arrow.fitness())[:args["amount"] if "amount" in args else 2]
        selectedPairs = []
        for i in range(len(arrows)):
            selected.append([random.randint(0,len(sortedArrows)-1 ), random.randint(0,len(sortedArrows)-1 )])
        return selectedPairs

    
def main():

main()

