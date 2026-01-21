def DisplayGrade(No):
    if(No > 75):
        print("Distinction.")

    elif(No >= 60):
        print("First Class")
    
    elif(No >= 50):
        print("Second Class")

    else:
        print("Fail")

def main():
    Value = int(input("Enter Marks: "))
    DisplayGrade(Value)

if __name__ == "__main__":
    main()
