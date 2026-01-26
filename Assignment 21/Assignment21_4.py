import threading

def Sum(numbers):
    print("Sum Thread ID:", threading.get_ident())
    print("Sum:", sum(numbers))

def Product(numbers):
    print("Product Thread ID:", threading.get_ident())
    result = 1
    for n in numbers:
        result *= n
    print("Product:", result)

def main():
    print("Main Thread ID:", threading.get_ident())
    numbers = [1, 2, 3, 4]

    t1 = threading.Thread(target=Sum, args=(numbers,))
    t2 = threading.Thread(target=Product, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()
