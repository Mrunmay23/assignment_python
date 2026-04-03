import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def MarvellousFakeNewsDetector(FakeFile, TrueFile):

    border = "-"*50

    # Step 1 : Load datasets
    print(border)
    print("Step 1 : Load Datasets")
    print(border)

    fake_df = pd.read_csv(FakeFile)
    true_df = pd.read_csv(TrueFile)

    print("Fake dataset shape :", fake_df.shape)
    print("True dataset shape :", true_df.shape)

    # Step 2 : Add labels
    print(border)
    print("Step 2 : Add Label Column")
    print(border)

    fake_df['label'] = 0
    true_df['label'] = 1

    # Step 3 : Combine datasets
    print(border)
    print("Step 3 : Combine datasets")
    print(border)

    df = pd.concat([fake_df, true_df], ignore_index=True)

    print("Combined dataset shape :", df.shape)

    # Step 4 : Select relevant column (text)
    print(border)
    print("Step 4 : Select Text Column")
    print(border)

    df = df[['text', 'label']]

    print(df.head())

    # Step 5 : Handle missing values
    print(border)
    print("Step 5 : Data Cleaning")
    print(border)

    df.dropna(inplace=True)

    print("After cleaning shape :", df.shape)

    # Step 6 : Feature Extraction (TF-IDF)
    print(border)
    print("Step 6 : TF-IDF Vectorization")
    print(border)

    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    X = vectorizer.fit_transform(df['text'])
    Y = df['label']

    print("Feature shape :", X.shape)

    # Step 7 : Train-Test Split
    print(border)
    print("Step 7 : Train Test Split")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    print("X_train :", X_train.shape)
    print("X_test :", X_test.shape)

    # Step 8 : Train Models
    print(border)
    print("Step 8 : Train Models")
    print(border)

    lr = LogisticRegression(max_iter=1000)
    dt = DecisionTreeClassifier()

    lr.fit(X_train, Y_train)
    dt.fit(X_train, Y_train)

    # Step 9 : Voting Classifier
    print(border)
    print("Step 9 : Voting Classifier")
    print(border)

    voting_hard = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='hard'
    )

    voting_soft = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='soft'
    )

    voting_hard.fit(X_train, Y_train)
    voting_soft.fit(X_train, Y_train)

    # Step 10 : Evaluation
    print(border)
    print("Step 10 : Evaluation")
    print(border)

    models = {
        "Logistic Regression": lr,
        "Decision Tree": dt,
        "Hard Voting": voting_hard,
        "Soft Voting": voting_soft
    }

    for name, model in models.items():

        print("\n----------------------------------")
        print("Model :", name)

        Y_pred = model.predict(X_test)

        print("Accuracy :", accuracy_score(Y_test, Y_pred))

        print("Confusion Matrix :")
        print(confusion_matrix(Y_test, Y_pred))

        print("Classification Report :")
        print(classification_report(Y_test, Y_pred))


def main():

    border = "-"*50

    print(border)
    print("Fake News Detection System")
    print(border)

    # IMPORTANT: Use your actual file names
    MarvellousFakeNewsDetector("fake.csv", "true.csv")


if __name__ == "__main__":
    main()