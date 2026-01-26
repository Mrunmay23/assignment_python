import threading

def Maximum(numbers):
    print("Maximum Thread ID:", threading.get_ident())
    print("Maximum number:", max(numbers))

def Minimum(numbers):
    print("Minimum Thread ID:", threading.get_ident())
    print("Minimum number:", min(numbers))

def main():
    print("Main Thread ID:", threading.get_ident())
    numbers = [10, 20, 5, 40]

    t1 = threading.Thread(target=Maximum, args=(numbers,))
    t2 = threading.Thread(target=Minimum, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()