import numpy as np
nrs = np.zeros((1,256), dtype=int)
iter=1
file=open('./rules.dat', 'w+')
c=""
for a1 in range(0,2):
    c1=str(a1)
    for a2 in range(0,2):
        c2=c1+str(a2)
        for a3 in range(0,2):
            c3=c2+str(a3)
            for a4 in range(0,2):
                c4=c3+str(a4)
                for a5 in range(0,2):
                    c5=c4+str(a5)
                    for a6 in range(0,2):
                        c6=c5+str(a6)
                        for a7 in range(0,2):
                            c7=c6+str(a7)
                            for a8 in range(0,2):
                                c8=c7+str(a8)
                                output=c8+","+str(iter)+'\n'
                                iter+=1
                                file.write(output)

