from functools import reduce

Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

FilterData = list(filter(lambda No : No % 2 == 0, Data))
print("List after filter :", FilterData)

MapData = list(map(lambda No : No * No, FilterData))
print("List after map :", MapData)

Result = reduce(lambda a, b : a + b, MapData)
print("Output of reduce :", Result)
