# Input : elements : 11
#Input elements :13 5 45 7 4 56 5 34 2 5 65
#Element of serch :5
#output 3

def Frequency(Arr, No):
    Count = 0
    for i in Arr:
        if i == No:
            Count = Count + 1
    return Count

def main():
    Size = int(input("Enter number of elements : "))
    Arr = []

    print("Enter elements :")
    for i in range(Size):
        Arr.append(int(input()))

    Value = int(input("Enter element to search : "))

    Ret = Frequency(Arr, Value)
    print("Frequency is :", Ret)

if __name__ == "__main__":
    main()
