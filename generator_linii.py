import numpy

def gen(a, b, c): #funkcja generująca wynik na podstawie sąsiadów
	return b

A = numpy.array([[1, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) #jakaś przykładowa macierz MxN
M=6 #liczba wierszy
N=5 #liczba kolumn


for i in range(0, M-2): #właściwa pętla dopisująca kolejny wiersz
		for j in range(0, N-1): # i numeruje wiersze, j kolumny
			if(j == 0):
				A[i+1][j] = gen(0, A[i][j], A[i][j+1])
			elif(j == N-1):
				A[i+1][j] = gen(A[i][j-1], A[i][j], 0)
			else:
				A[i+1][j] = gen(A[i][j-1], A[i][j], A[i][j+1])
