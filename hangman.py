import urllib
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

attempts = 0
randomWords = dict({})
mostFrequentWords = dict({})
alphabet = dict({})
whatTheComputerSees = []
usedLetters = []
computerChoosenChar = ""
SalsInput = ""


def enterWords():
    print("Enter Input")
    global whatTheComputerSees, SalsInput
    SalsInput = input()
    whatTheComputerSees = ["0"] * len(SalsInput)
    for x in range(len(SalsInput)):
        if SalsInput[x] == " ":
            whatTheComputerSees[x] = " "
    mainLoop()


def mainLoop():
    line = ""
    global attempts
    while attempts < 6:
        seperateWordsByTheSpace = 0
        global totalOccurances, total, computerChoosenChar
        totalOccurances = total = 0
        computerChoosenChar = ""
        for x in range(len(SalsInput)):
            theCharToBeExamined = SalsInput[x]
            print(x,len(SalsInput))
            if " " in theCharToBeExamined or x == len(SalsInput)-1:
                if whatTheComputerSees[seperateWordsByTheSpace:x].count("0") == 1:
                    line = line + theCharToBeExamined
                    computerPicksBasedOnOccurance(line, whatTheComputerSees[seperateWordsByTheSpace:x].index("0"))
                elif whatTheComputerSees[seperateWordsByTheSpace:x].count("0") == 2:
                    line = line + theCharToBeExamined
                    computerPicksBasedOnOccurance(line, whatTheComputerSees[seperateWordsByTheSpace:x].index("0"))
                elif whatTheComputerSees[seperateWordsByTheSpace:x].count("0") == 3:
                    line = line + theCharToBeExamined
                    computerPicksBasedOnOccurance(line, whatTheComputerSees[seperateWordsByTheSpace:x].index("0"))
                seperateWordsByTheSpace = x + 1
                addCharToAlphabets(line,x)
                line = ""
            else:
                line = line + theCharToBeExamined


def addCharToAlphabets(line,x):
    length = len(line)
    copyOfList = randomWords[length]

    for string in copyOfList:
        boolean = True
        for i in range(len(string)):
             if string[i] in usedLetters and string[i] != line[i]:
                 boolean = False
                 break
             if string[i] not in usedLetters and line[i] in usedLetters:
                 boolean = False
                 break
        if boolean == False:
            continue
        for y in range(len(string)):
            character = string[y]
            if character not in alphabet:
                alphabet[character] = 1
            else:
                # if string.find(character) != y:
                #     continue
                alphabet[character] += 1
    computerHoldsPercentage()


def computerHoldsPercentage():
    global totalOccurances, total, computerChoosenChar

    for char in alphabet:
        if char not in usedLetters:
            totalOccurances += alphabet[char]
    for anotChar in alphabet:
        if anotChar not in usedLetters:
            if total < alphabet[anotChar] / totalOccurances:
                total = alphabet[anotChar] / totalOccurances
                computerChoosenChar = anotChar
    computerPicks()


def computerPicks():
    atLeastOne = False
    global usedLetters

    for y in range(len(SalsInput)):
        character = SalsInput[y]
        if character.lower() == computerChoosenChar.lower():
            whatTheComputerSees[y] = computerChoosenChar
            atLeastOne = True

    if atLeastOne == False:
        global attempts
        attempts += 1
    usedLetters.append(computerChoosenChar)
    if "0" not in whatTheComputerSees:
        computerWon()
    print(whatTheComputerSees)
totalOccurances = total = 0


def computerWon():
    print(*whatTheComputerSees)
    print("Computer won" )
    quit()


def computerPicksBasedOnOccurance(line, index):
    boolean = False
    nextChar = 0
    while boolean == False:
        store = mostFrequentWords[len(line)]
        store = store[nextChar]
        nextChar += 1
        boolean = True
        for x in range(len(store)):
            if store[x].lower() in usedLetters and store[x].lower() != line[x].lower():
                boolean = False
                continue
            if store[x].lower() not in usedLetters and line[x].lower() in usedLetters:
                boolean = False
                continue
    global computerChoosenChar
    computerChoosenChar = store
    if (computerChoosenChar.lower() == SalsInput.lower()):
        whatTheComputerSees = SalsInput
    print(computerChoosenChar,SalsInput)
    computerChoosenChar = store[index]
    computerPicks()

def loadDataIntoDictionaries():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.strip().decode("utf-8")
        if len(decoded_line) not in randomWords:
            randomWords[len(decoded_line)] = []
            randomWords[len(decoded_line)].append(decoded_line)
        else:
            randomWords[len(decoded_line)].append(decoded_line)
    urlO = "https://gist.githubusercontent.com/h3xx/1976236/raw/bbabb412261386673eff521dddbe1dc815373b1d/wiki-100k.txt"
    fileO = urllib.request.urlopen(urlO)
    for lineO in fileO:
        decoded_lineO = lineO.strip().decode("utf-8")
        if len(decoded_lineO) not in mostFrequentWords:
            mostFrequentWords[len(decoded_lineO)] = []
            mostFrequentWords[len(decoded_lineO)].append(decoded_lineO)
        else:
            mostFrequentWords[len(decoded_lineO)].append(decoded_lineO)

loadDataIntoDictionaries()
enterWords()
print(whatTheComputerSees)
