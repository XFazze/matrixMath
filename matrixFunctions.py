from copy import deepcopy
import enum
from os import O_WRONLY
from exampleMatrixes import *


def add(a, b):
    if len(a) != len(b) and len(b) != 0:
        return False
    if len(a[0]) != len(b[0]) and len(b[0]) != 0:
        return False
    res = []
    for i, x in enumerate(a):
        t = []
        for ii, y in enumerate(x):
            t.append(y + b[i][ii])
        res.append(t)

    return res


def k(A, k):
    res = []
    for i in A:
        t = []
        for ii in i:
            t.append(ii*k)

        res.append(t)
    return res


def multi(A, B):
    if len(A) != len(B[0]):
        return False
    res = []
    for rowA in A:
        t = []
        for columnI in range(len(B[0])):
            x = 0
            for i, num in enumerate(rowA):
                x += num * B[i][columnI]
            t.append(x)
        res.append(t)

    return res


def t(A):
    res = deepcopy(A)
    for i in range(len(A)):
        for ii in range(len(A[0])):
            res[ii][i] = A[i][ii]

    return res


def p(A):
    for i in A:
        print(i)


# column by column
# pivot check
# inverse of number
# get zeros down rows

# row by row from bottom
# take row minus row below to get 0 0 1 0 if its the third row


def gaussEleminering(A, B):
    for columnI in range(len(A[0])):
        A, B = checkColumn(columnI, A, B)
        p(A)
        print(B)
        print('\n')
    print('going up again')
    for rowI in range(1, len(A)):
        rowI = len(A)-rowI-1
        A, B = checkRow(A, rowI, B)
        p(A)
        print(B)
        print('\n')


def checkRow(A, rowI, B):
    for i in range(rowI+1, len(A[rowI])):
        B[rowI][0] = B[rowI][0] + B[i][0] * A[rowI][i]
        A[rowI][i] = 0
    return A, B


def checkColumn(index, A, B):
    A = pivot(A, index)
    A, B = inverse(A, index, B)
    A = getZeros(A, index, B)
    return A, B


def pivot(A, index):
    if index == len(A) - 1:
        return A
    higest = [0, index, A[index]]
    for i in range(index, len(A)):
        if higest[0] < abs(A[i][index]):
            higest = [A[i][index], i, A[i]]
    A[higest[1]] = A[index]
    A[index] = higest[2]
    return A


def inverse(A, index, B):
    num = A[index][index]
    invNum = 1/num
    B[index][0] *= invNum
    row = []
    for i in A[index]:
        row.append(i*invNum)
    A[index] = row
    return A, B


def getZeros(A, index, B):
    for rowI in range(index+1, len(A)):
        amountMinus = A[rowI][index]/A[index][index]
        row = []
        for ii in range(len(A[rowI])):
            row.append(A[rowI][ii]-(A[index][ii]*amountMinus))
        A[rowI] = row
        B[rowI][0] -= amountMinus*B[index][0]
    return A


gaussEleminering(C3x3, CC3x1)
#p(add(k(A3x3, 3), k(B3x3, 2)))
#p(multi(A3x3, B3x3))
# p(t(A3x3))
