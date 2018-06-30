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
def evolve(A, N, M, rule):
    for i in range(0, M-1): #wlasciwa petla dopisujaca kolejny wiersz
         for j in range(0, N): # i numeruje wiersze, j kolumny
            if(j == 0):
                    A[i+1][j] = A[i][j]
            elif(j == N-1):
                    A[i+1][j] = A[i][j]
            else:
                    A[i+1][j] = gen(A[i][j-1], A[i][j], A[i][j+1], rule)
