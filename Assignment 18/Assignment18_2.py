# Input : elements : 7
#Input elements :13 5 45 7 4 56 34
#output 56

def Maximum(Arr):
    Max = Arr[0]
    for i in Arr:
        if i > Max:
            Max = i
    return Max

def main():
    Size = int(input("Enter number of elements : "))
    Arr = []

    print("Enter elements :")
    for i in range(Size):
        Arr.append(int(input()))

    Ret = Maximum(Arr)
    print("Maximum number is :", Ret)

if __name__ == "__main__":
    main()

