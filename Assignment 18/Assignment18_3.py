# Input : elements : 4
#Input elements :13 5 45 7 
#output 5



def Minimum(Arr):
    Min = Arr[0]
    for i in Arr:
        if i < Min:
            Min = i
    return Min

def main():
    Size = int(input("Enter number of elements : "))
    Arr = []

    print("Enter elements :")
    for i in range(Size):
        Arr.append(int(input()))

    Ret = Minimum(Arr)
    print("Minimum number is :", Ret)

if __name__ == "__main__":
    main()
