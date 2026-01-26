import threading

def Prime(numbers):
    print("Prime Thread ID:", threading.get_ident())
    for n in numbers:
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                print("Prime:", n)

def NonPrime(numbers):
    print("NonPrime Thread ID:", threading.get_ident())
    for n in numbers:
        if n <= 1:
            print("NonPrime:", n)
        else:
            for i in range(2, n):
                if n % i == 0:
                    print("NonPrime:", n)
                    break

def main():
    print("Main Thread ID:", threading.get_ident())
    numbers = [10, 11, 12, 13, 14, 15]

    t1 = threading.Thread(target=Prime, args=(numbers,))
    t2 = threading.Thread(target=NonPrime, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()
