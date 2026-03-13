from sklearn.linear_model import LinearRegression
import numpy as np

def PredictMarks():

    border = "-"*40

    X = np.array([1,2,3,4,5]).reshape(-1,1)
    Y = np.array([50,55,60,65,70])

    model = LinearRegression()

    model.fit(X,Y)

    prediction = model.predict([[6]])

    print(border)
    print("Predicted Marks for 6 study hours")
    print(border)

    print("Marks :",prediction[0])


def main():

    PredictMarks()


if __name__ == "__main__":
    main()