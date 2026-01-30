class Demo:
    Value = 0          # Class variable

    def __init__(self, A, B):
        self.no1 = A    # Instance variable
        self.no2 = B    # Instance variable

    def Fun(self):
        print("Inside Fun method")
        print("Value of no1 :", self.no1)
        print("Value of no2 :", self.no2)

    def Gun(self):
        print("Inside Gun method")
        print("Value of no1 :", self.no1)
        print("Value of no2 :", self.no2)


print("Class variable Value :", Demo.Value)

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
