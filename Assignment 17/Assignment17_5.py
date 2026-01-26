def CheckPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def main():
    Value = int(input("Enter number : "))
    if CheckPrime(Value):
        print("It is Prime Number")
    else:
        print("It is not Prime Number")

if __name__ == "__main__":
    main()


