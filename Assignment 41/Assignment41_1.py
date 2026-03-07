import math

def EucDistance(P1,P2):

    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)

    return Ans


def KNNClassifier():

    border = "-"*40

    data = [
            {'point':'A','X':1,'Y':2,'label':'Red'},
            {'point':'B','X':2,'Y':3,'label':'Red'},
            {'point':'C','X':3,'Y':3,'label':'Blue'},
            {'point':'D','X':6,'Y':5,'label':'Blue'}
           ]

    print(border)
    print("Training Data Set")
    print(border)

    for i in data:
        print(i)

    print(border)

    x = int(input("Enter X coordinate: "))
    y = int(input("Enter Y coordinate: "))

    new_point = {'X':x,'Y':y}

    # calculate distances
    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(border)
    print("Calculated Distances")
    print(border)

    for d in data:
        print(d['point'],"Distance:",round(d['distance'],2))

    sorted_data = sorted(data,key=lambda item:item['distance'])

    k = 3
    nearest = sorted_data[:k]

    print(border)
    print("Nearest Neighbors")
    print(border)

    votes = {}

    for d in nearest:
        print(d['point'],"Distance:",round(d['distance'],2))

        label = d['label']
        votes[label] = votes.get(label,0)+1

    predicted = max(votes,key=votes.get)

    print(border)
    print("Predicted Class:",predicted)


def main():

    KNNClassifier()


if __name__ == "__main__":
    main()