def Even(No):
    
    for i in range(2,No+1,2):    
        print(i,end=" ")

def main():
    Value = int(input("Enter Number : "))

    Even(Value)
    

if __name__ == "__main__":
    main()
