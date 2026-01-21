def Checkprime(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime:",n)

Checkprime(11)