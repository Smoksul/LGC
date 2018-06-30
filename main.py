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

M=512#liczba wierszy
N=256 #liczba kolumn
A = numpy.zeros((M,N), dtype='i') #macierz MxN inicjowana zerami
rd.setgen(A, N, cut.cut(111, 350))

for rlnbr in range(1,128):
    rule=rul.rules(rlnbr)
    cell.evolve(A, N, M, rule)
    plm.plot(A,rlnbr)
