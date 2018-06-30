import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

def plot(A):
    plt.matshow(A)
    plt.savefig("glider.png")