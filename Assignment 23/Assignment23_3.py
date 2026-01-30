class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are :", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total = total + i
        return total

    def ChkPerfect(self):
        if self.SumFactors() - self.Value == self.Value:
            return True
        else:
            return False


def main():
    num = int(input("Enter number : "))
    Obj = Numbers(num)

    if Obj.ChkPrime():
        print("Number is Prime")
    else:
        print("Number is Not Prime")

    if Obj.ChkPerfect():
        print("Number is Perfect")
    else:
        print("Number is Not Perfect")

    Obj.Factors()
    print("Sum of Factors :", Obj.SumFactors())


if __name__ == "__main__":
    main()
