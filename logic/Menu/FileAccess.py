
#Read the Names
def readNames():
    scoreName = open("Persistence/scoreName.txt", "r")
    return scoreName

#Read the Nums
def readNumbers():
    scoreNumber = open("Persistence/scoreNumbers.txt", "r")
    return scoreNumber

    
    

#Save the new Score
def saveScore(newScore):
    score = open("Persistence/scoreNumbers.txt", "a")
    score.write("\n"+str(newScore))
    score.close()

#Save the new Name
def saveName(newNames):
    names = open("Persistence/scoreName.txt", "a")
    names.write("\n"+newNames)
    names.close()