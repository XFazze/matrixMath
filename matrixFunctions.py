from copy import deepcopy
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


p(add(k(A3x3, 3), k(B3x3, 2)))
#p(multi(A3x3, B3x3))
# p(t(A3x3))
