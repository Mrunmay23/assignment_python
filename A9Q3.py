def Square(No):
        sqr = No * No
        return sqr
    
def main():
    Value = int(input("Enter number:"))
    
    Ret = Square(Value)
    print("Square of the number is: ",Ret)

if __name__ == "__main__":
    main()
