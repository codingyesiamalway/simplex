from Optimize import *

fileName = ""

for i in range(1, 100):
    fileDict = fileName + str(i) + '.dict'
    fileOut = fileName + str(i) + '.output'
    bv, nbv, b,A,z = getVariables(fileDict)
    r = init(bv, nbv, b,A,z)
    with open(fileOut) as f:
        line = f.readline()
        if r != line:
            print i, r, line
