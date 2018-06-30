import numpy

def gen(a, b, c): #funkcja generujaca wynik na podstawie sasiadow
	return b

A = numpy.array([[1, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) #jakas przykladowa macierz MxN
M=6 #liczba wierszy ktore beda PO wykonaniu petli
N=5 #liczba kolumn


for i in range(0, M-1): #wlasciwa petla dopisujaca kolejny wiersz
		A.resize((i+2, N))
		for j in range(0, N): # i numeruje wiersze, j kolumny
			if(j == 0):
				A[i+1][j] = A[i][j]
			elif(j == N-1):
				A[i+1][j] = A[i][j]
			else:
				A[i+1][j] = gen(A[i][j-1], A[i][j], A[i][j+1])
