def ChkPrime(No):
    if(No <= 1):
        return False
    for i in range(2,No):
        if(No % i == 0):
            return False

    else:
        return True
     
def main():
    Value = int(input("Enter Number: "))
    Ret = ChkPrime(Value)

    if(Ret == True):
        print("Prime Number")
    else:
        print("Not a prime Number")
