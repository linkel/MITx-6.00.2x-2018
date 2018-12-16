import random

def balls():
    bucket = [0, 0, 0, 1, 1, 1]
    grabbed = []
    grabbed.append(bucket.pop(random.randint(0,5)))
    grabbed.append(bucket.pop(random.randint(0,4)))
    grabbed.append(bucket.pop(random.randint(0,3)))
    for item in grabbed:
        if item != grabbed[0]:
            return False
    return True

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    same = 0
    for i in range(numTrials):
        if balls() == True:
            same += 1
    return same/numTrials



print(balls())