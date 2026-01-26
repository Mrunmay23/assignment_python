from functools import reduce

Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

FilterData = list(filter(lambda No : No >= 70 and No <= 90, Data))
print("List after filter :", FilterData)

MapData = list(map(lambda No : No + 10, FilterData))
print("List after map :", MapData)

Result = reduce(lambda a, b : a * b, MapData)
print("Output of reduce :", Result)
