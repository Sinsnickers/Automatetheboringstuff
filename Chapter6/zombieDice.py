import zombiedice

class twoRollsandRollAtZeroBrains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        thisZombie = gameState['CURRENT_ZOMBIE']
        highestScoreThatIsntMine = max([zombieScore for zombieName, zombieScore in gameState['SCORES'].items() if zombieName != thisZombie])
        diceRollResults = zombiedice.roll()
        #print(diceRollResults)
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults["brains"]
            #print(zombiedice.GAME_STATE)
            #if brains < 13 and highestScoreThatIsntMine >= 13:
               #diceRollResults = zombiedice.roll()
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

class importedZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            brains += diceRollResults["brains"]
            if brains <=3:
                diceRollResults = zombiedice.roll()
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.MonteCarloZombie(name='Monte Carlo40', riskiness=40, numExperiments=50),
    zombiedice.examples.MonteCarloZombie(name='Monte Carlo50', riskiness=50, numExperiments=50),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    twoRollsandRollAtZeroBrains(name='twoRollsandRollAtZeroBrains'),
    twoRollsandRollAtZeroBrainsAllIn(name="twoRollsandRollAtZeroBrainsAllIn"),
    importedZombie(name="importedZombie"),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1)
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