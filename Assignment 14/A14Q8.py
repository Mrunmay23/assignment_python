ChkDivisible = lambda x: (x % 3 == 0) and (x % 5 == 0)

def main():
    Data = [3,6,9,12,15,18,30]


    RData = list(filter(ChkDivisible,Data))
    print("list of numbers divisible by both 3 and 5:",RData)


if __name__ == "__main__":
    main()

