def Add(No1, No2):
    return No1 + No2

def main():
    A = int(input("Enter first number : "))
    B = int(input("Enter second number : "))
    Ret = Add(A, B)
    print("Addition is :", Ret)

if __name__ == "__main__":
    main()

