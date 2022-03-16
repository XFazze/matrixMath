from copy import deepcopy
from functions.basic import *

# column by column
# pivot check
# inverse of number
# get zeros down rows

# row by row from bottom
# take row minus row below to get 0 0 1 0 if its the third row


def gaussEleminering(A, B):
    for columnI in range(len(A[0])):
        A, B = checkColumn(columnI, A, B)

    for rowI in range(1, len(A)):
        rowI = len(A)-rowI-1
        A, B = checkRow(A, rowI, B)
    return A, B


def checkRow(A, rowI, B):
    for i in range(rowI+1, len(A[rowI])):
        B[rowI][0] = B[rowI][0] - B[i][0] * A[rowI][i]
        A[rowI][i] = 0
    return A, B


def checkColumn(index, A, B):
    A, B = pivot(A, index, B)
    A, B = inverse(A, index, B)
    A = getZeros(A, index, B)
    return A, B


def pivot(A, index, B):
    if index == len(A) - 1:
        return A, B
    higest = [0, index, A[index]]
    for i in range(index, len(A)):
        if higest[0] < abs(A[i][index]):
            higest = [A[i][index], i, A[i]]
    A[higest[1]] = A[index]
    A[index] = higest[2]
    Bsave = B[index]
    if higest[1] > len(B)-1:
        raise Exception('There is no solution')
    B[index] = B[higest[1]]
    B[higest[1]] = Bsave
    return A, B


def inverse(A, index, B):
    num = A[index][index]
    if num == 0:
        raise Exception('There is infinite solutions')
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
