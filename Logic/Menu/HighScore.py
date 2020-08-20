
posNew=[] #A list with the rank of players

#Organize the names of the Highscore and stablish them as String Variables
def organizeNames():
    scoreName = open("Persistence/scoreName.txt", "r")
    list = scoreName.read().split("\n")
    scoreString=""
    nameList=[]
    for i in list:
        nameList.append(i)  #Put the names in a list
    list=sortNames(nameList)
    for i in list:
        scoreString=scoreString+i+"\n"
    return scoreString

#Organize the Numbers of the Highscore and stablish them as String Variables
def organizeNumbers():
    scoreNumber = open("Persistence/scoreNumbers.txt", "r")
    list = scoreNumber.read().split("\n")
    scoreString=""
    scoreList=[]
    for i in list:
        scoreList.append(int(i)) #Put the score in a list
    list = sortScore(scoreList)
    for i in list:
        scoreString=scoreString+str(i)+"\n"
    return scoreString

#Sort Score (Upper to Lower)
def sortScore(scoreListOld):
    scoreList=sorted(scoreListOld, reverse=True)
    for i in range(len(scoreList)):
        posNew.append(scoreList.index(scoreListOld[i]))
    return scoreList

#Sort Names (Upper to Lower)
def sortNames(nameList,posiciones=posNew):
    nameListSorted=nameList.copy()
    for i in range(len(nameList)):
        if(i!=posiciones[i]):
            nameListSorted[posiciones[i]]=nameList[i]
    return nameListSorted