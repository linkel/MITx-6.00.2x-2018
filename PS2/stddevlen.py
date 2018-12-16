import math
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    item_lengths = []
    if len(L) == 0:
        return float('NaN')
    for item in L:
        item_lengths.append(len(item))
    # calculating mean
    sum = 0
    for item in item_lengths:
        sum += item
    mean = sum / len(item_lengths)
    sum_tu = 0
    for item in item_lengths:
        sum_tu += (item - mean)**2
    return math.sqrt(sum_tu / len(item_lengths))

teste = ['sp','spo','spadoo']
print(stdDevOfLengths(teste))