def gen(a, b, c, rule): #bierze sasiadow i numer reguly w postaci DZIESIETNEJ od 0 do 255
	tabv = [0,1,2,3,4,5,6,7] #tu sa loswe liczby, zaraz i tak beda nadpisane
	for i in range (0,8):
		tempr=int(rule)
		rule=int(rule)//2
		tabv[i]=tempr-rule*2
	return tabv[4*c+2*b+a]
