import math

def EucDistance(P1,P2):

    Ans = math.sqrt((P1['Study'] - P2['Study'])**2 + (P1['Attendance'] - P2['Attendance'])**2)

    return Ans

def StudentPrediction():

    data = [
            {'Study':2,'Attendance':60,'Result':'Fail'},
            {'Study':5,'Attendance':80,'Result':'Pass'},
            {'Study':6,'Attendance':85,'Result':'Pass'},
            {'Study':1,'Attendance':50,'Result':'Fail'}
           ]

    study = int(input("Enter Study Hours: "))
    attend = int(input("Enter Attendance: "))

    new_point = {'Study':study,'Attendance':attend}

    for d in data:
        d['distance'] = EucDistance(d,new_point)

    sorted_data = sorted(data,key=lambda item:item['distance'])

    k = 3

    nearest = sorted_data[:k]

    votes = {}

    for n in nearest:
        label = n['Result']
        votes[label] = votes.get(label,0)+1

    predicted = max(votes,key=votes.get)

    print("\nPredicted Result:",predicted)

def main():
    StudentPrediction()

if __name__ == "__main__":
    main()