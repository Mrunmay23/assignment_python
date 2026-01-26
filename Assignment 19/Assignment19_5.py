from functools import reduce

def CheckPrime(No):
    if No < 2:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

Data = [2, 70, 11, 10, 17, 23, 31, 77]

FilterData = list(filter(CheckPrime, Data))
print("List after filter :", FilterData)

MapData = list(map(lambda No : No * 2, FilterData))
print("List after map :", MapData)

Result = reduce(lambda a, b : a if a > b else b, MapData)
print("Output of reduce :", Result)