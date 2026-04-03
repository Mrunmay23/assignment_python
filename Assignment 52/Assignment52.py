import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def MarvellousStudentClustering(DataPath):

    border = "-"*50

    # Step 1 : Load dataset
    print(border)
    print("Step 1 : Load Dataset")
    print(border)

    try:
        df = pd.read_csv(DataPath, sep=';')   # UCI dataset
    except FileNotFoundError:
        print("ERROR : File not found ->", DataPath)
        print("Make sure CSV file is in same folder as Python file")
        return

    print("First 5 records:")
    print(df.head())

    print("\nColumns in dataset:")
    print(df.columns)

    # Step 2 : Select required features
    print(border)
    print("Step 2 : Select Features")
    print(border)

    df = df[['G1','G2','G3','studytime','failures','absences']]

    print(df.head())

    # Step 3 : Data Cleaning
    print(border)
    print("Step 3 : Data Cleaning")
    print(border)

    df.dropna(inplace=True)

    print("Shape :", df.shape)

    # Step 4 : Feature Scaling
    print(border)
    print("Step 4 : Feature Scaling")
    print(border)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    # Step 5 : Apply KMeans
    print(border)
    print("Step 5 : Apply KMeans")
    print(border)

    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    print("Clusters assigned")

    # Step 6 : Cluster Analysis
    print(border)
    print("Step 6 : Cluster Analysis")
    print(border)

    print(df.groupby('Cluster').mean())

    # Step 7 : Visualization
    print(border)
    print("Step 7 : Visualization")
    print(border)

    plt.scatter(df['G3'], df['studytime'], c=df['Cluster'])
    plt.xlabel("G3 (Final Grade)")
    plt.ylabel("Study Time")
    plt.title("Student Clustering")
    plt.show()

    # Step 8 : Interpretation
    print(border)
    print("Step 8 : Interpretation")
    print(border)

    print("Cluster 0 → Top Performers")
    print("Cluster 1 → Average Students")
    print("Cluster 2 → Struggling Students")


def main():

    border = "-"*50

    print(border)
    print("Student Performance Clustering System")
    print(border)

    MarvellousStudentClustering("student-mat.csv")


if __name__ == "__main__":
    main()