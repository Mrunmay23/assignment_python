def Table(No):
    
    for i in range(1,11):
        print( No * i,end=" ")
    
def main():
    Value = int(input("Enter Number : "))

    Table(Value)

if __name__ == "__main__":
    main()
