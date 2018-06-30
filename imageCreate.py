import matplotlib.pylab as plt
import numpy
import random

N = 720

a = numpy.zeros(N*N, dtype = 'i').reshape(N,N)

for x in range(0, N):
    for y in range(0, N):
        a[x][y] = random.randint(0,1)

labels = range(0, N)


fig = plt.figure()
plt.xticks(labels)
plt.imshow(a)

plt.show()
