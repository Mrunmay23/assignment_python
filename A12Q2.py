def Factors(No):
    for i in range(1,No+1):
        if(No % i == 0):
            print(i,end=" ")

def main():
    Value = int(input("Enter Number: "))
    
    Factors(Value)

if __name__ == "__main__":
    main()
