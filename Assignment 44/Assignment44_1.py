import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def MarvellousAdvertisingPredictor(DataPath):

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

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    print("Training completed successfully")


    print(border)
    print("Step 4 : Test Data")
    print(border)

    Y_pred = model.predict(X_test)


    print(border)
    print("Step 5 : Display predicted values and expected values")
    print(border)

    Result = pd.DataFrame({
        "Expected":Y_test,
        "Predicted":Y_pred
    })

    print(Result)



def main():

    border = "-"*40

    print(border)
    print("Marvellous Advertising Sales Predictor")
    print(border)

    MarvellousAdvertisingPredictor("Advertising.csv")


if __name__ == "__main__":
    main()