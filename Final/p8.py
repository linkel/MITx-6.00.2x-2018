import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP

    for _ in range(CURRENTRABBITPOP):
      born_chance = 1.0 - CURRENTRABBITPOP/MAXRABBITPOP
      if random.random() < born_chance:
        CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for _ in range(CURRENTFOXPOP):
      if CURRENTRABBITPOP <= 10:
        break
      elif CURRENTRABBITPOP > 10:
        eatChance = CURRENTRABBITPOP/MAXRABBITPOP
        if random.random() < eatChance:
          CURRENTRABBITPOP -= 1
          if random.random() < (1/3):
            CURRENTFOXPOP += 1
        else:
          if random.random() < (1/10):
            if CURRENTFOXPOP > 10:
              CURRENTFOXPOP -= 1

  
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for _ in range(numSteps):
      rabbitGrowth()
      foxGrowth()
      rabbit_populations.append(CURRENTRABBITPOP)
      fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)

rabbitPopulationOverTime, foxPopulationOverTime = runSimulation(200)

coeff = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)

pylab.plot(pylab.polyval(coeff, range(len(rabbitPopulationOverTime))))
pylab.show()

coeff2 = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)

pylab.plot(pylab.polyval(coeff2, range(len(foxPopulationOverTime))))
pylab.show()