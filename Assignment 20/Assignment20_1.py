import threading

def Even():
    print("Even Numbers:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()

def Odd():
    print("Odd Numbers:")
    for i in range(1, 20, 2):
        print(i, end=" ")
    print()

def main():
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
