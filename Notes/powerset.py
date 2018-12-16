# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

i = 4
j = 1
print(i >> j)

#print(1%2)
# from two bags


def powersetbag2(items):
"""
    Generates all combinations of N items into two bags, whereby each
    item is in one or zero bags.
    Yields a tuple, (bag1, bag2), where each bag is represented as a list
    of which item(s) are in each bag.
"""
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        firstbag = []
        secondbag = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 0:
                firstbag.append(items[j])
            elif (i // 3**j) % 3 == 1:
                secondbag.append(items[j])
            yield (firstbag, secondbag)