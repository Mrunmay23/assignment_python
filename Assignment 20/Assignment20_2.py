import threading

def EvenFactor(No):
    Sum = 0
    print("Even Factors:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print(i, end=" ")
            Sum += i
    print("\nSum of Even Factors:", Sum)

def OddFactor(No):
    Sum = 0
    print("Odd Factors:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print(i, end=" ")
            Sum += i
    print("\nSum of Odd Factors:", Sum)

def main():
    Value = int(input("Enter number : "))

    t1 = threading.Thread(target=EvenFactor, args=(Value,))
    t2 = threading.Thread(target=OddFactor, args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
