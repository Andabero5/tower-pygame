
#Organize the names of the Highscore and stablish them as String Variables
def organizeNames():
    scoreName = open("Persistence/scoreName.txt", "r")
    list = scoreName.read().split("\n")
    scoreString=""
    for i in list:
        scoreString=scoreString+i+"\n"
    return scoreString

#Organize the Numbers of the Highscore and stablish them as String Variables
def organizeNumbers():
    scoreNumber = open("Persistence/scoreNumbers.txt", "r")
    list = scoreNumber.read().split("\n")
    scoreString=""
    for i in list:
        scoreString=scoreString+i+"\n"
    return scoreString