from sklearn.linear_model import LinearRegression
import numpy as np

def StudyHoursRegression():

    border = "-"*40

    X = np.array([1,2,3,4,5]).reshape(-1,1)
    Y = np.array([50,55,60,65,70])

    print(border)
    print("Training Linear Regression Model")
    print(border)

    model = LinearRegression()

    model.fit(X,Y)

    print("Coefficient :",model.coef_)
    print("Intercept :",model.intercept_)


def main():

    StudyHoursRegression()


if __name__ == "__main__":
    main()