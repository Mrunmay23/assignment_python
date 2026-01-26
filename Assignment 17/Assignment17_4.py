def AddFactors(No):
    Sum = 0
    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i
    return Sum

def main():
    Value = int(input("Enter number : "))
    print(AddFactors(Value))

if __name__ == "__main__":
    main()


