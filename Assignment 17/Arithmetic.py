def Add(No1, No2):
    return No1 + No2

def Sub(No1, No2):
    return No1 - No2

def Mult(No1, No2):
    return No1 * No2

def Div(No1, No2):
    return No1 / No2


import Arithmetic

def main():
    A = int(input("Enter first number : "))
    B = int(input("Enter second number : "))

    print("Addition :", Arithmetic.Add(A, B))
    print("Subtraction :", Arithmetic.Sub(A, B))
    print("Multiplication :", Arithmetic.Mult(A, B))
    print("Division :", Arithmetic.Div(A, B))

if __name__ == "__main__":
    main()
