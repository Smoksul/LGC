import numpy
import random
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import randvec as rd
import cellmain as cell
import rulesmain as rul
import plotmain as plm
import cut
import big

#M=512#liczba wierszy
#N=256 #liczba kolumn

cutout = cut.cut(112,450)
#rd.setgen(A, N, vec)
BG = cut.findbg(cut.reduce(cutout, 100, 240))
#cutout = cut.cut(112, 0)
#vec=big.put(BG, cut.reduce(cutout, 75, 240))
#N=len(vec)
M=100
A = numpy.zeros((M,N), dtype='i') #macierz MxN inicjowana zerami
#rd.setgen(A, N, vec)
rd.randgen(A, N)

#for rlnbr in range(1,128):
rule=rul.rules(111)
cell.evolve(A, N, M, rule)
plm.plotspec(A, "show")
