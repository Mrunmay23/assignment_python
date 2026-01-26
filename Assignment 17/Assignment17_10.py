def SumDigits(No):
    Sum = 0
    while No > 0:
        Sum = Sum + (No % 10)
        No //= 10
    return Sum

def main():
    Value = int(input("Enter number : "))
    print(SumDigits(Value))

if __name__ == "__main__":
    main()
