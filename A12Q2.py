def main():
    n = int(input("Enter number: "))   # 12

    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")


if __name__ == "__main__":
    main()
