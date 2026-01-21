def ChkGreater(No1,No2):
    if(No1 > No2):
        return No1
    else:
        return No2
    
def main():
    Value1 = int(input("Enter first number:"))
    Value2 = int(input("Enter second number:"))
    
    Ret = ChkGreater(Value1,Value2)
    print("Greater value is: ",Ret)

if __name__ == "__main__":
    main()
