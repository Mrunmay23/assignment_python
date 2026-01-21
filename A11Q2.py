num = int(input())   # Input: 7521
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)         # Output: 4
