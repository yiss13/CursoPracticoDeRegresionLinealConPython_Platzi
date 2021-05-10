import numpy as np
import matplotlib.pyplot as plt


def estimateB0B1(x, y):
    # n = np.size(x)
    averageX = np.mean(x)
    averageY = np.mean(y)
    sumXY = np.sum((x - averageX) * (y - averageY))
    sumXX = np.sum(x * (x - averageX))
    b1 = sumXY / sumXX
    b0 = averageY - (b1 * averageX)

    return b1, b0


def plotRegression(x, y, b):
    plt.scatter(x, y, color = "g", marker = "o", s = 30)
    predY = b[0] + b[1] * x
    plt.plot(x, predY, color = "g")
    plt.xlabel("x-Independiente")
    plt.ylabel("y-Dependiente")
    plt.show()


def run():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 6, 5])
    b = estimateB0B1(x, y)

    print("Los valores de b0 = {}, b1 = {}".format(b[0], b[1]))

    plotRegression(x, y, b)


if __name__ == "__main__":
    run()