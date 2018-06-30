def gen(a, b, c, rule):
	tabv = [0,1,2,3,4,5,6,7]
	for i in range (0,8):
		tempr=int(rulenbr)
		rulenbr=int(rulenbr)//2
		tabv[i]=tempr-rulenbr*2
	return tabv[4*c+2*b+a]
