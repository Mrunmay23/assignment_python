import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score


def MarvellousBankClassifier(DataPath):

    border = "-"*50

    # Step 1 : Load Dataset
    print(border)
    print("Step 1 : Load and Explore Dataset")
    print(border)

    df = pd.read_csv(DataPath, sep=';')   # IMPORTANT

    print(df.head())
    print("\nShape :", df.shape)

    # Step 2 : Handle missing / unknown values
    print(border)
    print("Step 2 : Data Cleaning")
    print(border)

    df.replace("unknown", np.nan, inplace=True)
    df.dropna(inplace=True)

    print("After cleaning shape :", df.shape)

    # Step 3 : Convert target variable
    print(border)
    print("Step 3 : Convert Target Column")
    print(border)

    df['y'] = df['y'].map({'yes':1, 'no':0})

    # Step 4 : One-Hot Encoding
    print(border)
    print("Step 4 : Encoding categorical data")
    print(border)

    df = pd.get_dummies(df, drop_first=True)

    print("Encoding completed")

    # Step 5 : Separate X and Y
    print(border)
    print("Step 5 : Split features and target")
    print(border)

    X = df.drop('y', axis=1)
    Y = df['y']

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    # Step 6 : Train-Test Split
    print(border)
    print("Step 6 : Train Test Split")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42, stratify=Y
    )

    print("X_train :", X_train.shape)
    print("X_test :", X_test.shape)

    # Step 7 : Feature Scaling
    print(border)
    print("Step 7 : Feature Scaling")
    print(border)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Scaling done")

    # Step 8 : Train Models
    print(border)
    print("Step 8 : Train Models")
    print(border)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Random Forest": RandomForestClassifier()
    }

    results = {}

    for name, model in models.items():

        print("\n----------------------------------")
        print("Training :", name)

        model.fit(X_train_scaled, Y_train)
        Y_pred = model.predict(X_test_scaled)

        acc = accuracy_score(Y_test, Y_pred)
        roc = roc_auc_score(Y_test, Y_pred)

        results[name] = acc

        print("Accuracy :", acc)
        print("ROC-AUC :", roc)

        print("Confusion Matrix :")
        print(confusion_matrix(Y_test, Y_pred))

        print("Classification Report :")
        print(classification_report(Y_test, Y_pred))

    # Step 9 : Compare Models
    print(border)
    print("Step 9 : Model Comparison")
    print(border)

    for name, acc in results.items():
        print(name, "Accuracy :", acc)

    # Step 10 : Plot Graph
    print(border)
    print("Step 10 : Accuracy Comparison Graph")
    print(border)

    plt.figure(figsize=(8,5))
    plt.bar(results.keys(), results.values())
    plt.title("Model Accuracy Comparison")
    plt.xlabel("Models")
    plt.ylabel("Accuracy")
    plt.show()


def main():

    border = "-"*50

    print(border)
    print("Bank Marketing Prediction System")
    print(border)

    MarvellousBankClassifier("bank-full.csv")   # Make sure file is correct


if __name__ == "__main__":
    main()