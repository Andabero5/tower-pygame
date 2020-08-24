
from singleton import *
from Menu.FileAccess import*

posNew=[] #A list with the rank of players

#Organize the names of the Highscore and stablish them as String Variables
def organizeNames():
    list = readNames().read().split("\n")
    nameList=[]
    for i in list:
        nameList.append(i)  #Put the names in a list
    return sortNames(nameList)

#Covert a list in a String (Names)
def namesToString(list):
    scoreString=""
    for i in list:
        scoreString=scoreString+i+"\n"
    return scoreString

#Covert a list in a String (Numbers)
def numsToString(list):
    scoreString=""
    for i in list:
        scoreString=scoreString+str(i)+"\n"
    return scoreString

#Organize the Numbers of the Highscore and stablish them as String Variables
def organizeNumbers():
    list = readNumbers().read().split("\n")
    scoreString=""
    scoreList=[]
    for i in list:
        scoreList.append(int(i)) #Put the score in a list
    return sortScore(scoreList)

#Sort Score (Upper to Lower)
def sortScore(scoreListOld):
    scoreList=sorted(scoreListOld, reverse=True)
    for i in range(len(scoreList)):
        posNew.append(scoreList.index(scoreListOld[i]))
    scoreListTop=scoreList[:5]
    return scoreListTop

#Sort Names (Upper to Lower)
def sortNames(nameList,posiciones=posNew):
    nameListSorted=nameList.copy()
    for i in range(len(nameList)):
        if(i!=posiciones[i]):
            nameListSorted[posiciones[i]]=nameList[i]
    nameListTop=nameListSorted[:5]
    return nameListTop
