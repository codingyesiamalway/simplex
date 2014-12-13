__author__ = 'Yu Zhao'
from Optimize import *

fileName = "C:\Users\Yu Zhao\PycharmProjects\untitled\part3TestCases\part3TestCases\\unitTests\\10\\test"
for i in range(1, 100):
    fileDict = fileName + str(i) + '.dict'
    fileOut = fileName + str(i) + '.output'
    bv, nbv, b,A,z = getVariables(fileDict)
    r = init(bv, nbv, b,A,z)
    with open(fileOut) as f:
        print i, r, f.readline()

