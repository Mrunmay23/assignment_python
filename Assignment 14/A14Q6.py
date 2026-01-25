from functools import reduce

Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Data = [11,22,101,45,54,]

    RData = reduce(Minimum,Data)
    print("Minimum from numbers are:",RData)


if __name__ == "__main__":
    main()