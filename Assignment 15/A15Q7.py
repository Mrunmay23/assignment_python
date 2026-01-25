ChkDivisible = lambda No1: No1 % 5 == 0 

def main():
    Value = int(input("Enter Number: "))

    Ret = ChkDivisible(Value)
    print("is Divisible by 5:",Ret)

if __name__ == "__main__":
    main()