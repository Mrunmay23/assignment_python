import numpy as np

def CalculateStats():

    border = "-"*40

    data = [6,7,8,9,10,11,12]

    variance = np.var(data)
    std = np.std(data)

    print(border)
    print("Variance :",variance)
    print("Standard Deviation :",std)


def main():

    CalculateStats()


if __name__ == "__main__":
    main()