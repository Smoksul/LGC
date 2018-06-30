import numpy
import random
import matplotlib.pylab as plt


M=50 #liczba wierszy ktore beda PO wykonaniu petli
N=100 #liczba kolumn

A = numpy.zeros(N*M, dtype='i').reshape(M,N)

for x in range(0, M):
    for y in range(0, N):
        A[x][y] = random.randint(0,1)

#labels = range(0,N)
#plt.xticks(labels)
plt.matshow(A)
plt.imshow(A)
plt.show()
