from exampleMatrixes import gauss, basic
from functions.basic import *
from functions.gaussElimination import *

A, B = gaussEleminering(gauss.EL, gauss.ER)
#r = add(k(A3x3, 3), k(B3x3, 2))
#r = multi(A3x3, B3x3)
#r = t(A3x3)

# p(r)
pp(A, B)
