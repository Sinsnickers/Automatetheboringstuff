import zombiedice

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        print("First Hand" + str(zombiedice.GAME_STATE["CURRENT_HAND"]))
        diceRollResults = zombiedice.roll()
        print("Second Hand" + str(zombiedice.GAME_STATE["CURRENT_HAND"]))
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            #print(zombiedice.GAME_STATE)
            if shotguns  <2:
                diceRollResults = zombiedice.roll() # roll again
            elif (shotguns==2) and ("red" in zombiedice.GAME_STATE["CURRENT_HAND"]):
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

zombies = (
    #zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    #zombiedice.examples.MonteCarloZombie(name='Monte Carlo40', riskiness=40, numExperiments=50),
    #zombiedice.examples.MonteCarloZombie(name='Monte Carlo50', riskiness=50, numExperiments=50),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)

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