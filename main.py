import numpy
import random
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import randvec as rd
import cellmain as cell
import rulesmain as rul
import plotmain as plm

M=1024 #liczba wierszy
N=256 #liczba kolumn
rlnbr=input("Podaj numer zasady.")
A = numpy.zeros((M,N), dtype='i') #macierz MxN inicjowana zerami
rule=rul.rules(rlnbr)
rd.randgen(A,N)
cell.evolve(A, N, M, rule)
plm.plot(A)
