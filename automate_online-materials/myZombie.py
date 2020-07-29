import zombiedice

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
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
            elif (shotguns<=2) and not ("red" in zombiedice.GAME_STATE["CURRENT_HAND"]):
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    #zombiedice.examples.MonteCarloZombie(name='Monte Carlo40', riskiness=40, numExperiments=50),
    #zombiedice.examples.MonteCarloZombie(name='Monte Carlo50', riskiness=50, numExperiments=50),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=500)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
