import random
def randgen(A, N):
    random.seed()
    for i in range (0,N):
        A[0][i]=random.randint(0,1)
def setgen(A, N, setvec):
    for i in range (0,N):
        A[0][i]=setvec[i]