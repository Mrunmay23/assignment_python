class BankAccount:
    ROI = 10.5   # Class variable

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Account Balance     :", self.Amount)

    def Deposit(self):
        value = int(input("Enter amount to deposit : "))
        self.Amount = self.Amount + value

    def Withdraw(self):
        value = int(input("Enter amount to withdraw : "))
        if value <= self.Amount:
            self.Amount = self.Amount - value
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    Obj1 = BankAccount("Mrunmay", 10000)

    Obj1.Display()
    Obj1.Deposit()
    Obj1.Display()
    Obj1.Withdraw()
    Obj1.Display()

    print("Calculated Interest :", Obj1.CalculateInterest())


if __name__ == "__main__":
    main()
