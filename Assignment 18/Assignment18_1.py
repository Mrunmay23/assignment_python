# Input : elements : 6
#Input elements :13 5 45 7 4 56
#output 130

def AddElements(Arr):
    Sum = 0
    for i in Arr:
        Sum = Sum + i
    return Sum

def main():
    Size = int(input("Enter number of elements : "))
    Arr = []

    print("Enter elements :")
    for i in range(Size):
        Arr.append(int(input()))

    Ret = AddElements(Arr)
    print("Addition is :", Ret)

if __name__ == "__main__":
    main()
