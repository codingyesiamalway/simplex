__author__ = 'Yu Zhao'

from pivot import *

fileName = "C:\Users\Yu Zhao\PycharmProjects\untitled\part2TestCases\part2TestCases\unitTests\dict10"
#fileName = "C:\Users\Yu Zhao\PycharmProjects\untitled\part2TestCases\part2TestCases\\assignmentParts\part1.dict"

def oneStepPivot(bv, nbv, b,A,z):
    enterVarIndex,enterPosIndex =  getEnter(bv, nbv, b,A,z)
    if enterVarIndex == -1:
        print "UNBOUNDED"
        return None
    leaveVar, leavePos, objectIncrease = getLeave(bv, nbv, b,A,z, enterVarIndex, enterPosIndex)
    if leaveVar == 99999:
        print "UNBOUNDED"
        return None

    for i in range(0, len(z) - 1):
        if i != enterPosIndex:
            A[leavePos][i] = A[leavePos][i] /  A[leavePos][enterPosIndex] * -1.0
            z[i + 1] = z[i + 1] + A[leavePos][i] * z[enterPosIndex + 1]

    b[leavePos] = float(b[leavePos]) /  A[leavePos][enterPosIndex] * -1.0
    A[leavePos][enterPosIndex] = 1.0 / A[leavePos][enterPosIndex]
    bv[leavePos] = enterVarIndex

    nbv[enterPosIndex] = leaveVar
    z[enterPosIndex + 1] = z[enterPosIndex + 1] * A[leavePos][enterPosIndex]
    z[0] = z[0] + objectIncrease
    return bv, nbv, b,A,z

def optimize(bv, nbv, b,A,z):
    step = 0
    positive = True
    while True:
        positve = False
        for i in range(0, len(z) - 1):
            if z[i + 1] > 0:
                positve = True
                break
        if not positve:
            return bv, nbv, b,A,z, step
        else:
            bv, nbv, b,A,z = oneStepPivot(bv, nbv, b,A,z)
        step = step + 1

    return bv, nbv, b,A,z, step + 1

bv, nbv, b,A,z = getVariables(fileName)
bv, nbv, b,A,z, step = optimize(bv, nbv, b,A,z)

print z[0], step


