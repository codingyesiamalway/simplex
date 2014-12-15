from pivot import *

fileName = ""

def oneStepPivot(bv, nbv, b,A,z):
    enterVarIndex,enterPosIndex =  getEnter(bv, nbv, b,A,z)
    if enterVarIndex == -1:
        return bv, nbv, b,A,z
    leaveVar, leavePos, objectIncrease = getLeave(bv, nbv, b,A,z, enterVarIndex, enterPosIndex)
    if leaveVar == 99999:
        return -1, -1, -1, -1, -1

    for i in range(0, len(z) - 1):
        if i != enterPosIndex:
            A[leavePos][i] = A[leavePos][i] /  A[leavePos][enterPosIndex] * -1.0
            z[i + 1] = z[i + 1] + A[leavePos][i] * z[enterPosIndex + 1]
    b[leavePos] = float(b[leavePos]) / A[leavePos][enterPosIndex] * -1.0
    A[leavePos][enterPosIndex] = 1.0 / A[leavePos][enterPosIndex]

    for i in range(0, len(A)):
        if i != leavePos:
            for j in range(0, len(z) - 1):
                if j != enterPosIndex:
                    A[i][j] = A[i][j] + A[i][enterPosIndex] * A[leavePos][j]
            b[i] = b[i] + b[leavePos] * A[i][enterPosIndex]

    for i in range(0, len(A)):
        if i != leavePos:
            A[i][enterPosIndex] = A[i][enterPosIndex] * A[leavePos][enterPosIndex]

    bv[leavePos] = enterVarIndex
    nbv[enterPosIndex] = leaveVar
    z[enterPosIndex + 1] = z[enterPosIndex + 1] * A[leavePos][enterPosIndex]
    z[0] = z[0] + objectIncrease
    return bv, nbv, b, A, z

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
            if bv == -1:
                return -1, -1, -1, -1, -1, -1
        step = step + 1
    return bv, nbv, b,A,z, step + 1

def getDual(bv, nbv, b, A, z):
    dualz = [-1 * i for i in b]
    dualz.insert(0, -1 * z[0])
    dualb = [-1 * i for i in z]
    dualb.pop(0)

    dualNbv = []
    dualBv = []

    for i in range(0, len(bv)):
        dualNbv.append(bv[i])
    for j in range(0, len(nbv)):
        dualBv.append(nbv[j])
    dualA = [[-1 * j[i] for j in A] for i in range(len(A[0]))]
    return dualBv, dualNbv, dualb, dualA, dualz

def init(bv, nbv, b,A,z):
    newZ = [-1 for i in z]
    newZ[0] = 0
    dualBv, dualNbv, dualb, dualA, dualz = getDual(bv, nbv, b, A, newZ)
    bvFinalDual, nbvFinalDual, bFinalDual, AFinalDual, zFinalDual, steps= optimize(dualBv, dualNbv, dualb, dualA, dualz)
    if bvFinalDual == -1:
        #print "INFEASIBLE"
        return "INFEASIBLE"
    bvOrig, nbvOrig, bOrig, AOrig, zOrig = getDual(bvFinalDual, nbvFinalDual, bFinalDual, AFinalDual, zFinalDual)

    newz = []
    for i in nbv:
        if i in bvOrig:
            rowInA = bvOrig.index(i)
            pos = nbv.index(i)
            tmpz = []
            tmpz.append(z[pos + 1] * bOrig[rowInA])
            for j in range(1, len(z)):
                tmpz.append(z[pos + 1] * AOrig[rowInA][j - 1])
            newz.append(tmpz)

    aggregatedNewZ = []
    if len(newz) > 0:
        for i in range(0, len(newz[0])):
            sum = 0
            for j in range(0, len(newz)):
                sum = sum + newz[j][i]
            aggregatedNewZ.append(sum)

    if len(aggregatedNewZ) == 0:
        aggregatedNewZ = list(z)
        for i in range(0, len(z)):
            if nbv[i - 1] in nbvOrig:
                index = nbvOrig.index(nbv[i - 1])
                aggregatedNewZ[index + 1] = z[i]
    else:
        aggregatedNewZ[0] = aggregatedNewZ[0] + z[0]
        for i in range(1, len(z)):
            if nbv[i - 1] in nbvOrig:
                index = nbvOrig.index(nbv[i - 1])
                aggregatedNewZ[index + 1] = aggregatedNewZ[index + 1] + z[i]
    bvFinal, nbvFinal, bFinal, AFinal, zFinal, steps= optimize(bvOrig, nbvOrig, bOrig, AOrig, aggregatedNewZ)
    if zFinal == -1:
        #print "UNBOUNDED"
        return "UNBOUNDED"
    else:
        return bvFinal, nbvFinal, bFinal, AFinal, zFinal

bv, nbv, b,A,z = getVariables(fileName)
# print init(bv, nbv, b, A, z)


