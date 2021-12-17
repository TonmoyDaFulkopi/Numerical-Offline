import numpy as np
import matplotlib.pyplot as plt


def func_ret(x):
    return x ** 3 - 18 * (x ** 2) + 475.2


def bisect_method(low, up, error, maxi):
    mid1 = (low + up) / 2

    for i in range(maxi - 1):
        f1 = func_ret(low)
        f2 = func_ret(mid1)
        if f1 * f2 > 0:
            low = mid1
        elif f1 * f2 < 0:
            up = mid1

        mid2 = (low + up) / 2

        e = abs(mid1 - mid2) * 100 / mid2
        if e < error:
            return mid2
        else:
            mid1 = mid2


x = np.arange(0, 18, 0.05)
y = func_ret(x)


def graph_show():
    l1 = [0, 20]
    l2 = [0, 0]
    l3 = [0, 0]
    l4 = [-550, 550]

    v1 = [0, 0]
    v2 = [0, func_ret(0)]
    v3 = [12, 12]
    v4 = [0, func_ret(12)]

    plt.plot(v1, v2, "r")
    plt.plot(v3, v4, "r")

    plt.plot(l1, l2, "b")
    plt.xlabel("Value of x")
    plt.ylabel("Value of y")
    plt.title("Graph of f(x)")
    plt.plot(x, y, "b")
    plt.plot(l1, l2, "k")
    # plt.plot(l3, l4, "k")
    plt.show()


def table_show(low, up, error, maxi):
    j = 1
    mid1 = (low + up) / 2
    e = "N/A"

    lst1 = [[mid1, j, e]]

    for i in range(maxi - 1):
        j += 1
        f1 = func_ret(low)
        f2 = func_ret(mid1)
        if f1 * f2 > 0:
            low = mid1
        elif f1 * f2 < 0:
            up = mid1

        mid2 = (low + up) / 2

        e = abs(mid1 - mid2) * 100 / mid2
        lst1.append([j,mid2,e])

        mid1 = mid2

    val1 = ["Iteration No.", "Approx. Root", "Error %"]

    fig, ax = plt.subplots(1, 1)
    ax.axis("tight")
    ax.axis("off")
    table = ax.table(cellText=lst1, colLabels=val1, colColours=["palegreen"] * 10, cellLoc='center', loc='upper left')
    table.set_fontsize(20)
    table.scale(1, 1.15)
    ax.set_title('Table of Absolute Relative Error Approx. for each step', fontweight="bold")

    plt.show()


graph_show()

print("approximate value of the root:", round(bisect_method(0, 12, 0.5, 20), 3))
table_show(0, 12, 0.5, 20)

