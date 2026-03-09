import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def MarvellousPlayPredictor(DataPath):

    border = "-"*40

    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entry from dataset")
    print(df.head())
    print(border)


    print(border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(border)

    df.dropna(inplace=True)

    le = LabelEncoder()

    df["Whether"] = le.fit_transform(df["Whether"])
    df["Temperature"] = le.fit_transform(df["Temperature"])
    df["Play"] = le.fit_transform(df["Play"])

    print("Encoded Dataset")
    print(df)
    
    print(border)
    print("Step 3 : Train Data using KNN")
    print(border)

    X = df[["Whether","Temperature"]]
    Y = df["Play"]

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X,Y)

    print("Training completed successfully")


    print(border)
    print("Step 4 : Test Data")
    print(border)

    Whether = int(input("Enter Whether value : "))
    temperature = int(input("Enter Temperature value : "))

    result = model.predict([[Whether,temperature]])

    if(result[0] == 1):
        print("Prediction : Yes")
    else:
        print("Prediction : No")

    CheckAccuracy(X,Y)

def CheckAccuracy(X,Y):

    border = "-"*40

    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    K_values = range(1,6)

    for k in K_values:

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test,Y_pred)

        print("Accuracy for K =",k,"is :",accuracy*100)

def main():

    border = "-"*40

    print(border)
    print("Marvellous Play Predictor using KNN")
    print(border)

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()