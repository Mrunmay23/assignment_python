import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def KNNPrediction():

    data = [
            {'point':'A','X':1,'Y':2,'label':'Red'},
            {'point':'B','X':2,'Y':3,'label':'Red'},
            {'point':'C','X':3,'Y':3,'label':'Blue'},
            {'point':'D','X':6,'Y':5,'label':'Blue'}
           ]

    new_point = {'X':2,'Y':2}

    for d in data:
        d['distance'] = EucDistance(d,new_point)

    sorted_data = sorted(data,key=lambda item:item['distance'])

    print("Prediction Results\n")

    for k in [1,3,4]:

        nearest = sorted_data[:k]

        votes = {}

        for n in nearest:
            label = n['label']
            votes[label] = votes.get(label,0)+1

        predicted = max(votes,key=votes.get)

        if k == 4:
            print("K = 5 ->",predicted)
        else:
            print("K =",k,"->",predicted)

def main():
    KNNPrediction()

if __name__ == "__main__":
    main()