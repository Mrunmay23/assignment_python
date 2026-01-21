def Sum(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + i
    print("Sum of numbers is: ", Sum)
    
def main():
    Value = int(input("Enter Number : "))

    Sum(Value)

if __name__ == "__main__":
    main()
