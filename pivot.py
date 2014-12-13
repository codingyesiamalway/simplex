__author__ = 'Yu Zhao'


#fileName = "C:\Users\Yu Zhao\PycharmProjects\untitled\part1TestCases\part1TestCases\unitTests\dict7"
def getVariables(fileName):
    line  = 0
    A = []
    m = 0
    with open(fileName) as f:
        content = f.readlines()
        for lineStr in content:
            toks = lineStr.split()
            if line == 0:
                m = int(toks[0])
                n = int(toks[1])
            elif line == 1:
                bv = [float(i) for i in toks]
            elif line == 2:
                nbv =  [float(i) for i in toks]
            elif line == 3:
                b =  [float(i) for i in toks]
            elif line >= 4 and line <= m + 3:
                A.append([float(i) for i in toks])
            elif line == m + 4:
                z = [float(i) for i in toks]
            line = line + 1
    return bv, nbv, b,A,z

def getEnter(bv, nbv, b,A,z):
    enterIndex = -1
    posIndex = -1
    for i in range(0, len(nbv)):
        if z[i + 1] > 0 and ( enterIndex == -1 or nbv[i] < enterIndex):
            enterIndex = nbv[i]
            posIndex = i
    return enterIndex, posIndex

def getLeave(bv, nbv, b,A,z, enterVarIndex, enterPosIndex):
    leaveVar = 99999
    leavePos = 0
    objectIncrease = 99999
    for i in range(0, len(b)):
        if A[i][enterPosIndex] < 0 and b[i] >= 0:
            if (objectIncrease > b[i] / A[i][enterPosIndex] * -1) or (objectIncrease == b[i] / A[i][enterPosIndex] * -1 and bv[i] < leaveVar):
                objectIncrease = b[i] / A[i][enterPosIndex] * -1.0
                leaveVar = bv[i]
                leavePos = i
    return leaveVar, leavePos, objectIncrease * z[enterPosIndex + 1]

