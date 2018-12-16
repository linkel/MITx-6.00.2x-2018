import numpy as np

# from itertools explanation of itertools.product
def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = list(map(tuple, args)) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
        
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    power_set = []
    for i in product([0,1],repeat = len(choices)):
        power_set.append(np.array(i))
    equal_to_total = []
    less_than_total = []
    for possibility in power_set:
        if sum(possibility*choices) == total:
            equal_to_total.append(possibility)
        elif sum(possibility*choices) < total:
            less_than_total.append(possibility)
    if len(equal_to_total) > 0:
        #for ct, val in (enumerate(equal_to_total)):
        #    print(ct,val)
        my_set = min(enumerate(equal_to_total),key = lambda x :sum(x[1]))
        result = my_set[1]
    else:
        #for ct, val in (enumerate(less_than_total)):
        #    print(ct,val)
        my_set = max(enumerate(less_than_total),key = lambda x :sum(x[1]))
        result = my_set[1]
    
    return result

#If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
#If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
#If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]

choices = [1,1,1,9]
total = 4
print(find_combination(choices, total))  