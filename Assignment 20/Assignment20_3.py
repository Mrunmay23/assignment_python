import threading

def EvenList(Data):
    Sum = 0
    print("Even Elements:")
    for i in Data:
        if i % 2 == 0:
            print(i, end=" ")
            Sum += i
    print("\nSum of Even Elements:", Sum)

def OddList(Data):
    Sum = 0
    print("Odd Elements:")
    for i in Data:
        if i % 2 != 0:
            print(i, end=" ")
            Sum += i
    print("\nSum of Odd Elements:", Sum)

def main():
    Size = int(input("Enter number of elements : "))
    Data = []

    for i in range(Size):
        Data.append(int(input("Enter element : ")))

    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
