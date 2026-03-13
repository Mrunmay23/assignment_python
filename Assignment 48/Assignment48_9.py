from sklearn.metrics import classification_report

def GenerateReport():

    border = "-"*40

    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    print(border)
    print("Classification Report")
    print(border)

    print(classification_report(actual,predicted))


def main():

    GenerateReport()


if __name__ == "__main__":
    main()