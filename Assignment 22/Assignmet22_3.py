class Arithmetic:
    def Accept(self, A, B):
        self.Value1 = A
        self.Value2 = B

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Division by zero not allowed"


No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

obj = Arithmetic()
obj.Accept(No1, No2)

Ans = obj.Addition()
print("Addition is :", Ans)

Ans = obj.Subtraction()
print("Subtraction is :", Ans)

Ans = obj.Multiplication()
print("Multiplication is :", Ans)

Ans = obj.Division()
print("Division is :", Ans)
