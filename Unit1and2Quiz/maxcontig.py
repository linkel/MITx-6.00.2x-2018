testList = [3, 4, -8, 15, -1, 2]
# max sum is 16 (15 -1 2)

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    outersum = 0
    for i in range(len(L)):
        innersum = 0
        savedinnerSum = 0
        for j in range(i, len(L)):
            innersum += L[j]
            if innersum > savedinnerSum:
                savedinnerSum = innersum
        if savedinnerSum > outersum:
            outersum = savedinnerSum
    return outersum

print(max_contig_sum(testList))