#Code by Benji Christie

#Input the name of a volleyball player, then the specific stat associated to the
#player and the amount of times they do that thing

def validateName(prompt):
    while True:
        try:
            name = input(prompt)
            if(not (name.isalpha())):
                raise NameError
            break
        except NameError:
            prompt = "Invalid Name...Please enter a name with only letters:\n"
    return name

def validateNum(prompt):
    while True:
        try:
            num = int(input(prompt))
            if(num < 0):
                raise ValueError
            break
        except ValueError:
            prompt = "Please enter a positive number\n"
    return num

def getName():
    numPlayers = int(input("How many player's will you be entering stats for?\n"))
    namesBank = []
    prompt = "Please enter the player's name: "
    for i in range(0,numPlayers):
        name = validateName(prompt)
        namesBank.append(name)
    return namesBank

def getStats(stats,name):
    numStats=[]
    for i in range(0,len(stats)):
        prompt = "How many "+ stats[i] +" did "+name+" get?\n"
        num = validateNum(prompt)
        numStats.append(num)
    return numStats

def setStats(stat,num):
    totalStat = {}
    for i in range(0,len(stat)):
        totalStat.update({stat[i]:num[i]})
    return totalStat

def createPlayerBase(names,stats):
    players = {}
    for i in range(0,len(names)):
        numStats = getStats(stats, names[i])
        players[names[i]] = setStats(stats,numStats)
    return players

#main
names = getName()
stats = ['kills','blocks','digs']
players = createPlayerBase(names,stats)
print(players)
