def ModelPerformance():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    m = 0.4
    c = 2.4

    Y_pred = []

    print("Predicted Y values:")

    for i in X:
        pred = m*i + c
        Y_pred.append(pred)
        print("X =",i,"Predicted Y =",round(pred,2))

    # MSE
    mse = 0

    for i in range(len(Y)):
        mse = mse + (Y[i]-Y_pred[i])**2

    mse = mse/len(Y)

    print("\nMean Squared Error =",round(mse,3))

    # R2 score

    mean_y = sum(Y)/len(Y)

    ss_total = 0
    ss_res = 0

    for i in range(len(Y)):
        ss_total = ss_total + (Y[i]-mean_y)**2
        ss_res = ss_res + (Y[i]-Y_pred[i])**2

    r2 = 1 - (ss_res/ss_total)

    print("R2 Score =",round(r2,3))


def main():
    ModelPerformance()

if __name__ == "__main__":
    main()