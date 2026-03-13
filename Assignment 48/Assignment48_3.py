from sklearn.preprocessing import StandardScaler

def FeatureScaling():

    border = "-"*40

    data = [[25,20000],
            [30,40000],
            [35,80000]]

    print(border)
    print("Original Data")
    print(data)

    scaler = StandardScaler()

    scaled = scaler.fit_transform(data)

    print(border)
    print("Scaled Data")
    print(scaled)


def main():

    FeatureScaling()


if __name__ == "__main__":
    main()