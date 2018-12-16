from ps1_partition import get_partitions
import time
from ps1 import load_cows
import os

os.chdir(".") 
myDict = load_cows("ps1_cow_data.txt")

def brute_force(cows,limit=10):
    curr_smallest = float('Inf')
    for partition in get_partitions(cows):
        exceeded_limit = False
        for subtrips in partition:
            subtrip_weight = 0
            for cow in subtrips:
                subtrip_weight = subtrip_weight + cows[cow]
            if subtrip_weight > limit:
                exceeded_limit = True
                break
        if exceeded_limit == False and len(partition) < curr_smallest:
            curr_smallest = len(partition)
            chosen = partition
    return chosen

print(brute_force(myDict, 10))