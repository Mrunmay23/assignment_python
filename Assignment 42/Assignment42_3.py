import matplotlib.pyplot as plt

def SalaryPrediction():

    experience = [1,2,3,4,5]
    salary = [20000,25000,30000,35000,40000]

    n = len(experience)

    mean_x = sum(experience)/n
    mean_y = sum(salary)/n

    num = 0
    den = 0

    for i in range(n):
        num += (experience[i]-mean_x)*(salary[i]-mean_y)
        den += (experience[i]-mean_x)**2

    m = num/den
    c = mean_y - m*mean_x

    x_new = 6
    predicted_salary = m*x_new + c

    print("Predicted Salary for 6 Years Experience: ₹",int(predicted_salary))

    # Plot graph
    plt.scatter(experience,salary)

    y_line = []

    for x in experience:
        y_line.append(m*x + c)

    plt.plot(experience,y_line)

    plt.xlabel("Experience")
    plt.ylabel("Salary")

    plt.show()


def main():
    SalaryPrediction()

if __name__ == "__main__":
    main()