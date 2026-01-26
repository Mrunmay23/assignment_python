def CountDigits(No):
    count = 0
    while No > 0:
        count += 1
        No //= 10
    return count

def main():
    Value = int(input("Enter number : "))
    print(CountDigits(Value))

if __name__ == "__main__":
    main()

