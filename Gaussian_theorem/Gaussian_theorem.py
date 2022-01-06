import numpy as np
import sys

# prevent numpy exponential notation on print, default False
np.set_printoptions(suppress=True)

n = int(input("Enter number of unknowns: "))

A = np.zeros((n, n))
B = np.zeros(n)
# The answer 1D matrix
x = np.zeros(n)

print("Enter Coefficients: ")

for i in range(n):
    for j in range(n):
        A[i][j] = float(input("A[" + str(i) + "][" + str(j) + "]="))

print("Enter Constants:")
for i in range(n):
    B[i] = float(input("B[" + str(i) + "]="))

# function to show both matrices
def show_mats(a):
    A = np.zeros((n, n))
    B = np.zeros(n)
    for i in range(n):
        for j in range(n):
            A[i][j] = a[i][j]

    for i in range(n):
        B[i] = a[i][n]

    print("A: ", "\n", A, "\n")
    print("B: ", "\n", B, "\n")


def GaussianElimination(A, B, pivot, showall):

    a = np.zeros((n, n + 1))
    x = np.zeros(n)

    for i in range(n):
        for j in range(n):
            a[i][j] = A[i][j]

    for i in range(n):
        a[i][n] = B[i]

    # Checking if any is 0
    # Getting ratio
    for i in range(n):
        # Row Swapping
        if pivot == True:
            max = abs(a[i][i])
            index = i
            for j in range(i + 1, n):
                if abs(a[j][i]) > max:
                    max = abs(a[j][i])
                    index = j

            # swapping
            for j in range(i, n + 1):
                a[i][j], a[index][j] = a[index][j], a[i][j]

        # Notice: Realize that only the Diagonals are divided therefore a[i][i]
        if a[i][i] == 0.0:
            print("Division by zero detected!")
            sys.exit()

        # Forward elimination of unknowns
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

        # Print arrays
        if showall != False and i != n - 1:
            print("Forward Elimination no.", i + 1, sep="")
            show_mats(a)

    # Back Substitution
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    return x


x = GaussianElimination(A, B, True, True)

print("Solution: ")
for i in range(n):
    print("X%d = %0.4f" % (i + 1, x[i]))
