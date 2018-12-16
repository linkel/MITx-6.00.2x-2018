import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, normed=True, bins=numBins)
    pylab.ylabel(yLabel)
    pylab.xlabel(xLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest_run_list = []
    for _ in range(numTrials):
        rolls = []
        for _ in range(numRolls):
            rolls.append(die.roll())
        #print(rolls)
        longest_run_list.append(longestrun(rolls))
    #print(longest_run_list)
    makeHistogram(longest_run_list, 10, "Longest Runs","Longest Runs")
    average = sum(longest_run_list)/len(longest_run_list)
    return average

#rolltest = [5,6,6,7,7,7,7,8]
def longestrun(rolls):
    longestRoll = None
    currRoll = None
    run_length = 0
    longest_run_length = 0
    for roll in rolls:
        if currRoll != roll:
            currRoll = roll
            run_length = 0
        if currRoll == roll:
            run_length += 1
        if run_length > longest_run_length:
            longest_run_length = run_length
    return longest_run_length

# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 5, 1))