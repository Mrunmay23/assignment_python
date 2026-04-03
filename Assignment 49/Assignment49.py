import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):

    border = "-"*40 

    # Step 1 : Load dataset
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print("First 5 records : ")
    print(df.head())

    # Step 2 : Data Cleaning
    print(border)
    print("Step 2 : Data Cleaning")
    print(border)

    df.dropna(inplace=True)

    cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
    for col in cols:
        df[col] = df[col].replace(0, df[col].mean())

    print("Total records :", df.shape[0])
    print("Total columns :", df.shape[1])

    # Step 3 : Separate X and Y
    print(border)
    print("Step 3 : Separate independent and dependent variables")
    print(border)

    X = df.drop(columns=['Outcome'])
    Y = df['Outcome']

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    print("Input Columns :", X.columns.to_list())   # ✅ fixed ()
    print("Output Column : Outcome")

    # Step 4 : Train Test Split
    print(border)
    print("Step 4 : Split dataset")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42, stratify=Y
    )

    print("X_train :", X_train.shape)
    print("X_test :", X_test.shape)
    print("Y_train :", Y_train.shape)
    print("Y_test :", Y_test.shape)

    # Step 5 : Feature Scaling
    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)   # ✅ corrected

    print("Feature scaling completed")

    # Step 6 : Hyperparameter tuning
    print(border)
    print("Step 6 : Hyperparameter tuning (K values)")
    print(border)

    accuracy_scores = []
    K_values = list(range(1, 21))

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, Y_train)

        Y_pred = model.predict(X_test_scaled)
        acc = accuracy_score(Y_test, Y_pred)
        accuracy_scores.append(acc)

    print("Accuracy for K values :")
    for i in range(len(K_values)):
        print("K =", K_values[i], "Accuracy =", accuracy_scores[i])

    # Step 7 : Plot Graph
    print(border)
    print("Step 7 : Plot K vs Accuracy")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values, accuracy_scores, marker='o')
    plt.title("K vs Accuracy")
    plt.xlabel("K value")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.show()

    # Step 8 : Best K
    print(border)
    print("Step 8 : Find best K")
    print(border)

    best_k = K_values[accuracy_scores.index(max(accuracy_scores))]   # ✅ fixed
    print("Best K value is :", best_k)

    # Step 9 : Final Model
    print(border)
    print("Step 9 : Build Final Model")
    print(border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled, Y_train)

    Y_pred = final_model.predict(X_test_scaled)

    # Step 10 : Accuracy
    print(border)
    print("Step 10 : Final Accuracy")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy :", accuracy * 100)

    # Step 11 : Confusion Matrix
    print(border)
    print("Step 11 : Confusion Matrix")
    print(border)

    cm = confusion_matrix(Y_test, Y_pred)
    print(cm)

    # Step 12 : Classification Report
    print(border)
    print("Step 12 : Classification Report")
    print(border)

    print(classification_report(Y_test, Y_pred))


def main():

    border = "-"*40

    print(border)
    print("Diabetes Predictor Using KNN")
    print(border)

    MarvellousClassifier("diabetes.csv")   # make sure file exists


if __name__ == "__main__":
    main()