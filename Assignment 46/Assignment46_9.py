from sklearn.linear_model import LinearRegression
import numpy as np

def MultipleRegression():

    border = "-"*40

    X = np.array([
        [1,7],
        [2,6],
        [3,7],
        [4,6],
        [5,8]
    ])

    Y = np.array([50,55,60,65,70])

    print(border)
    print("Training Multiple Linear Regression Model")
    print(border)

    model = LinearRegression()

    model.fit(X,Y)

    print("Coefficients :",model.coef_)
    print("Intercept :",model.intercept_)


def main():

    MultipleRegression()


if __name__ == "__main__":
    main()