import numpy
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import random


def rules(): #pobiera zasade
	rulenbr=0
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


M=1024 #liczba wierszy
N=256 #liczba kolumn
A = numpy.zeros((M,N), dtype='i') #macierz MxN inicjowana zerami

random.seed()
for i in range (0,N):
	A[0][i]=random.randint(0,1)



rule=rules()

print A
for i in range(0, M-1): #wlasciwa petla dopisujaca kolejny wiersz
		for j in range(0, N): # i numeruje wiersze, j kolumny
			if(j == 0):
				A[i+1][j] = A[i][j]
			elif(j == N-1):
				A[i+1][j] = A[i][j]
			else:
				A[i+1][j] = gen(A[i][j-1], A[i][j], A[i][j+1], rule)

plt.matshow(A)
plt.savefig("glider.png")