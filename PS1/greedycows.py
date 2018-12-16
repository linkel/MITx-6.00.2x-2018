cowdict = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}

def greedy_cow_transport(D, weight_limit):
    sortedValues = sorted(D.values(), reverse=True)
    tripList = []
    flatTripList = []
    while len(flatTripList) < len(D):
        subtrip = []
        current_weight = 0
        for i in range(len(sortedValues)):
            bigHolder = sortedValues[i]
            for k, v in D.items():
                if (v == bigHolder) and (current_weight + v <= weight_limit) and (k not in flatTripList):
                    subtrip.append(k)
                    flatTripList.append(k)
                    current_weight = v + current_weight
        tripList.append(subtrip)
    return tripList




print(greedy_cow_transport(cowdict, 10))