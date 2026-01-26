# Input : elements : 11
#Input elements :13 5 45 7 4 56 10 34 2 5 8
#output 32

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def ListPrime(Arr):
    Sum = 0
    for i in Arr:
        if ChkPrime(i):
            Sum = Sum + i
    return Sum

def main():
    Size = int(input("Enter number of elements : "))
    Arr = []

    print("Enter elements :")
    for i in range(Size):
        Arr.append(int(input()))

    Ret = ListPrime(Arr)
    print("Addition of prime numbers is :", Ret)

if __name__ == "__main__":
    main()
