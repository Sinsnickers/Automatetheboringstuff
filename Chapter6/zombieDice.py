import zombiedice

def yellowInCup():
    yellow = 0
    for color in zombiedice.GAME_STATE["CURRENT_CUP"]:
        if color == "yellow":
            yellow += 1
    return yellow

def greenInCup():
    green = 0
    for color in zombiedice.GAME_STATE["CURRENT_CUP"]:
        if color == "green":
            green += 1
    return green

def redDice():
    red = 0
    for dice in zombiedice.GAME_STATE["CURRENT_HAND"]:
        if dice=="red":
            red += 1
    return red

def greenDice():
    green = 0
    for dice in zombiedice.GAME_STATE["CURRENT_HAND"]:
        if dice=="green":
            green += 1
    return green

def yellowDice():
    yellow = 0
    for dice in zombiedice.GAME_STATE["CURRENT_HAND"]:
        if dice=="yellow":
            yellow += 1
    return yellow
            
    

class twoRollsandRollAtZeroBrains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        thisZombie = gameState['CURRENT_ZOMBIE']
        highestScoreThatIsntMine = max([zombieScore for zombieName, zombieScore in gameState['SCORES'].items() if zombieName != thisZombie])
        diceRollResults = zombiedice.roll()
        #print(zombiedice.GAME_STATE["CURRENT_CUP"])
        
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults["brains"]
            if shotguns  <2:
                diceRollResults = zombiedice.roll() # roll again
            elif shotguns == 2 and brains == 0:
                diceRollResults = zombiedice.roll()
            else:
                break

class twoRollsandRollAtZeroBrainsAllIn:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        thisZombie = gameState['CURRENT_ZOMBIE']
        highestScoreThatIsntMine = max([zombieScore for zombieName, zombieScore in gameState['SCORES'].items() if zombieName != thisZombie])
        diceRollResults = zombiedice.roll()
        
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults["brains"]
            if brains <= 12 and highestScoreThatIsntMine >= 13:
               diceRollResults = zombiedice.roll()
            elif shotguns  <2:
                diceRollResults = zombiedice.roll() # roll again
            elif shotguns == 2 and brains == 0:
                diceRollResults = zombiedice.roll()
            else:
                break

class fullAlgo:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        brains = 0
        diceRollResults = zombiedice.roll()
        while(diceRollResults is not None):
            shotguns += diceRollResults["shotgun"]
            brains += diceRollResults["brains"]
            #print(zombiedice.GAME_STATE["CURRENT_CUP"])
            red = redDice()
            green = greenDice()
            yellow = yellowDice()
            yellowIn = yellowInCup()
            greenIn = greenInCup()
            if shotguns == 0:
                diceRollResults = zombiedice.roll()
            elif shotguns == 1:
                if brains >= 2 and ((red == 2 and yellow == 1) or (yellowIn > greenIn)):
                    break
                elif brains >= 3 and ((red == 2 and green == 1) or (greenIn > yellowIn)):
                    break
                elif red ==3:
                    break
                elif green == 3:
                    diceRollResults = zombiedice.roll()
                else:
                    diceRollResults = zombiedice.roll()
            elif shotguns == 2:
                if brains == 0:
                    diceRollResults = zombiedice.roll()
                elif brains < 2 and green == 3:
                    print("greenTwoNutter")
                    diceRollResults = zombiedice.roll()
                else:
                    break
            else:
                break
class partAlgo:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        brains = 0
        diceRollResults = zombiedice.roll()
        while(diceRollResults is not None):
            shotguns += diceRollResults["shotgun"]
            brains += diceRollResults["brains"]
            #print(zombiedice.GAME_STATE["CURRENT_CUP"])
            red = redDice()
            green = greenDice()
            yellow = yellowDice()
            yellowIn = yellowInCup()
            greenIn = greenInCup()
            if shotguns == 0:
                diceRollResults = zombiedice.roll()
            elif shotguns == 1:
                if brains >= 2 and red == 2 and yellow == 1:
                    break
                elif brains >= 3 and red == 2 and green == 1:
                    break
                elif red ==3:
                    break
                elif green == 3:
                    diceRollResults = zombiedice.roll()
                else:
                    diceRollResults = zombiedice.roll()
            elif shotguns == 2:
                if brains == 0:
                    diceRollResults = zombiedice.roll()
                elif brains < 2 and green == 3:
                    print("greenTwoNutter")
                    diceRollResults = zombiedice.roll()
                else:
                    break
            else:
                break
                
class partAlgo2:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        brains = 0
        diceRollResults = zombiedice.roll()
        while(diceRollResults is not None):
            shotguns += diceRollResults["shotgun"]
            brains += diceRollResults["brains"]
            #print(zombiedice.GAME_STATE["CURRENT_CUP"])
            red = redDice()
            green = greenDice()
            yellow = yellowDice()
            yellowIn = yellowInCup()
            greenIn = greenInCup()
            if shotguns == 0:
                diceRollResults = zombiedice.roll()
            elif shotguns == 1:
                if brains >= 2 and yellowIn > greenIn:
                    break
                elif brains >= 3 and greenIn > yellowIn:
                    break
                elif red ==3:
                    break
                elif green == 3:
                    diceRollResults = zombiedice.roll()
                else:
                    diceRollResults = zombiedice.roll()
            elif shotguns == 2:
                if brains == 0:
                    diceRollResults = zombiedice.roll()
                elif brains < 2 and green == 3:
                    print("greenTwoNutter")
                    diceRollResults = zombiedice.roll()
                else:
                    break
            else:
                break
                

zombies = (
    #zombiedice.examples.MonteCarloZombie(name='Monte Carlo40', riskiness=40, numExperiments=50),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    twoRollsandRollAtZeroBrains(name='twoRollsandRollAtZeroBrains'),
    #twoRollsandRollAtZeroBrainsAllIn(name="twoRollsandRollAtZeroBrainsAllIn"),
    fullAlgo(name="fullAlgo"),
    partAlgo(name="partAlgo"),
    partAlgo2(name="partAlgo2"),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=100000)
#zombiedice.runWebGui(zombies=zombies, numGames=100000)

#TODO Try to implement the optimal strat
#Current Shotguns Rule
#0 shotguns Always keep rolling.
#1 shotguns
#If we must roll 3 red dice, stop at 1 brain.
#If (rf = 2 and yf = 1) or yc > gc, stop at 2 brains.
#If (rf = 2 and gf = 1) or gc > yc, stop at 3 brains.
#If we must roll 3 green dice, roll again.
#If gf = 2, roll again.
#2 shotguns
#With gf = 3, stop at 2 brains.
#Otherwise, stop at 1 brain.
