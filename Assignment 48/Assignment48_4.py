import numpy as np
from sklearn.preprocessing import StandardScaler

def EuclideanDistance():

    border = "-"*40

    p1 = [25,20000]
    p2 = [35,80000]

    print(border)
    print("Points :",p1,p2)

    before = np.linalg.norm(np.array(p1)-np.array(p2))

    scaler = StandardScaler()

    data = [p1,p2]

    scaled = scaler.fit_transform(data)

    after = np.linalg.norm(scaled[0]-scaled[1])

    print("Distance before scaling :",before)
    print("Distance after scaling :",after)


def main():

    EuclideanDistance()


if __name__ == "__main__":
    main()