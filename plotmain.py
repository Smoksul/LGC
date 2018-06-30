import matplotlib
import numpy
matplotlib.use('pdf')
import matplotlib.pyplot as plt

def plot(A,rlnbr):
    plt.matshow(A)
    numpy.savetxt("../out/out_"+str(rlnbr)+".dat", A, fmt = '%i')
    plt.savefig("../out/out_"+str(rlnbr)+".png")
