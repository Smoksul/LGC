def rules(nbr): #pobiera zasade
	rulenbr=nbr
	tempstr=""
	file=open('./rules.dat', 'r') #otwiera plik z zasadami
	for helpiter in range(1,257):	#iteracja po liniach
		line=file.readline()
		if helpiter==rulenbr:
			for iter1 in range(0, 8):
				tempstr=tempstr+line[iter1]
			return tempstr