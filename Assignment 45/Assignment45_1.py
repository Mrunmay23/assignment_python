import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


def MarvellousWineClassifier(DataPath):

    border = "-"*40

    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)

    print(border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(border)

    df.dropna(inplace=True)

    print("Total Records :",df.shape[0])
    print("Total Columns :",df.shape[1])

    print(border)
    print("Step 3 : Train Data")
    print(border)

    X = df.drop(columns=["Class"])
    Y = df["Class"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train_scaled,Y_train)

    print("Training completed successfully")

    print(border)
    print("Step 4 : Test Data")
    print(border)

    Y_pred = model.predict(X_test_scaled)

    print("Predicted Values : ")
    print(Y_pred)

    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy of model is :",accuracy*100)

def main():

    border = "-"*40

    print(border)
    print("Marvellous Wine Classifier using KNN")
    print(border)

    MarvellousWineClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()