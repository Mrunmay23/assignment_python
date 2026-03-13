def StandardScaling():

    border = "-"*40

    mean = 9
    std = 2

    numbers = [6,9,12]

    print(border)
    print("Standard Scaling Calculation")
    print(border)

    for num in numbers:

        scaled = (num - mean) / std

        print("Original :",num," Scaled :",scaled)


def main():

    StandardScaling()


if __name__ == "__main__":
    main()