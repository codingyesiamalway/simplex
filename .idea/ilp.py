from pivot import *
from Optimize import *

fileName = "C:\Users\Yu Zhao\PycharmProjects\untitled\ilpTests\ilpTests\unitTests\ilpTest0"

bv, nbv, b,A,z = getVariables(fileName)
bvFinal, nbvFinal, bFinal, AFinal, zFinal = init(bv, nbv, b, A, z)
