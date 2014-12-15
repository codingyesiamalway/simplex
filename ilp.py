from Optimize import *
from pivot import *
from math import *


fileName = "/home/yuzhao/projects/simplex/ilpTests/ilpTests/unitTests/test0"
bv, nbv, b,A,z = getVariables(fileName)

UNBOUNDED = "UNBOUNDED"
INFEASIBLE = "INFEASIBLE"

def isInteger(a):
    return abs(round(a, 0) - a) < 0.00001

def getNonIntegerPos(l):
    indexList = []
    for i in range(0, len(l)):
        if not isInteger[i]:
            indexList.append(i)
    return indexList

def getLargest(bv, nbv):
    largest = 0
    for i in bv + nbv:
        if i > largest:
            largest = i
    return largest


def ilp(bv, nbv, b,A,z, curBestObj):
    #bvFinal, nbvFinal, bFinal, AFinal, zFinal = init(bv, nbv, b,A,z)
    if bv == UNBOUNDED or bv == INFEASIBLE:
        return bv
    nonIntVarIndecies = getNonIntegerPos(b)
    if len(nonIntVarIndecies) == 0:
        return z[0]
    else:
        minObj = curBestObj
        nonIntVarIndex = nonIntVarIndecies[0]

        # smaller than floor value
        bvLower, nbvLower, bLower, ALower, zLower = list(bv), list(nbv), list(b), list(A), list(z)
        bvLower.append(getLargest(bvLower, nbvLower) + 1)
        newRowA = [ -1 * i for i in ALower[nonIntVarIndex]]
        ALower.append(newRowA)
        bLower.append(-1 * bLower[nonIntVarIndex] + floor(bLower[nonIntVarIndex]))
        bvLowerOpt, nbvLowerOpt, bLowerOpt, ALowerOpt, zLowerOpt = init( bvLower, nbvLower, bLower, ALower, zLower)







