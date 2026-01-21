# input 123
print("Enter Number :")
n = int(input())

rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

print(rev)
#output 321