import numpy as np

def LinearRegression():

    border = "-"*40

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print(border)
    print("Dataset")
    print(border)

    print("X =",X)
    print("Y =",Y)

    n = len(X)

    mean_x = sum(X)/n
    mean_y = sum(Y)/n

    print("\nMean of X =",mean_x)
    print("Mean of Y =",mean_y)

    num = 0
    den = 0

    for i in range(n):
        num = num + (X[i]-mean_x)*(Y[i]-mean_y)
        den = den + (X[i]-mean_x)**2

    m = num/den
    c = mean_y - m*mean_x

    print("\nSlope (m) =",round(m,1))
    print("Intercept (c) =",round(c,1))

    print("\nRegression Equation:")
    print("Y =",round(m,1),"X +",round(c,1))

    x_new = 6
    y_pred = m*x_new + c

    print("\nPredicted Y for X = 6 :",round(y_pred,1))


def main():
    LinearRegression()

if __name__ == "__main__":
    main()