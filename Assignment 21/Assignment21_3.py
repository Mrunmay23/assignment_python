import threading

count = 0
lock = threading.Lock()

def Increment():
    global count
    print("Thread ID:", threading.get_ident())
    for i in range(5):
        lock.acquire()
        count += 1
        lock.release()

def main():
    print("Main Thread ID:", threading.get_ident())

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Count:", count)
    print("End of main")

if __name__ == "__main__":
    main()
