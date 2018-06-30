import numpy
import matplotlib.pylab as plt


def rules(): #pobiera zasade
	rulenbr=0
	tempstr=""
	rulenbr=input('Wpisz numer zasady: ')
	while (rulenbr<1) and (rulenbr>255) :
		rulenbr=input('Wpisz numer zasady: ') #idiotouodparnianie
	file=open('/rules.dat', 'w+') #otwiera plik z zasadami
	helpiter=1
	for line in file:	#iteracja po liniach
		if helpiter==rulenbr:
			for iter1 in range (0,len(line)): #iteracja po wyrazach linii
				while line[iter1]!=',':
					tempstr=tempstr+line[iter1]
				return tempstr
		helpiter+=1



def gen(a, b, c, rule): #funkcja generujaca wynik na podstawie sasiadow
	if a:
		if b:
			if c:
				return int(rule[1])
			else:
				return int(rule[2])
		else:
			if c:
				return int(rule[3])
			else:
				return int(rule[4])
	else:
		if b:
			if c:
				return int(rule[5])
			else:
				return int(rule[6])
		else:
			if c:
				return int(rule[7])
			else:
				return int(rule[8])


A = numpy.array([[1, 0, 1, 0, 0, 0, 1, 0, 1, 1]]) #jakas przykladowa macierz MxN
M=30 #liczba wierszy ktore beda PO wykonaniu petli
N=10 #liczba kolumn

rule=rules()
for i in range(0, M-1): #wlasciwa petla dopisujaca kolejny wiersz
		A.resize((i+2, N))
		for j in range(0, N): # i numeruje wiersze, j kolumny
			if(j == 0):
				A[i+1][j] = A[i][j]
			elif(j == N-1):
				A[i+1][j] = A[i][j]
			else:
				A[i+1][j] = gen(A[i][j-1], A[i][j], A[i][j+1], rule)

