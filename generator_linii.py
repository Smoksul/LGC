import numpy
import linecache


def rules(): #pobiera zasade
	rulenbr=10
	tempstr=""
	rulenbr=input('Wpisz numer zasady: ')
	while (rulenbr<1) and (rulenbr>255) :
		rulenbr=input('Wpisz numer zasady: ') #idiotouodparnianie
	file=open('./rules.dat', 'r') #otwiera plik z zasadami
	helpiter=1
	for helpiter in range(1,257):	#iteracja po liniach
		line=file.readline()
		if helpiter==rulenbr:
			for iter1 in range(0, 8):
				tempstr=tempstr+line[iter1]
			return tempstr

def gen(a, b, c, rule): #funkcja generujaca wynik na podstawie sasiadow
	if a:
		if b:
			if c:
				return int(rule[0])
			else:
				return int(rule[1])
		else:
			if c:
				return int(rule[2])
			else:
				return int(rule[3])
	else:
		if b:
			if c:
				return int(rule[4])
			else:
				return int(rule[5])
		else:
			if c:
				return int(rule[6])
			else:
				return int(rule[7])


A = numpy.array([[1, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) #jakas przykladowa macierz MxN
M=6 #liczba wierszy
N=5 #liczba kolumn

rule=rules()
for i in range(0, M-1): #wlasciwa petla dopisujaca kolejny wiersz
		for j in range(0, N): # i numeruje wiersze, j kolumny
			if(j == 0):
				A[i+1][j] = A[i][j]
			elif(j == N-1):
				A[i+1][j] = A[i][j]
			else:
				A[i+1][j] = gen(A[i][j-1], A[i][j], A[i][j+1], rule)
