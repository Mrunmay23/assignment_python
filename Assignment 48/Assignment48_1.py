import numpy as np

def CalculateMean():

    border = "-"*40

    data = [6,7,8,9,10,11,12]

    print(border)
    print("Dataset :",data)
    print(border)

    mean = np.mean(data)

    print("Mean of dataset :",mean)


def main():

    CalculateMean()


if __name__ == "__main__":
    main()