import numpy

def cut(rlchoice, linechoice):
    fname="../out/out_"+str(rlchoice)+".dat"
    file=open(fname)
    refline=""
    iter=0
    while iter!=linechoice:
        file.readline()
        iter+=1
    line=file.readline()
    for iter1 in range(0, len(line)-1):
        if line[iter1]!=' ':
            refline=refline+line[iter1]
    return refline

def reduce(row, beg, end):
    result = ""
    for i in range(beg,end):
        result += row[i]
    return result

def findbg(row):
    for iter in range(3, len(row)):
        tr=1
        for iter2 in range(0, iter):
            if row[0+iter2]!=row[iter+iter2]:
                tr=0
                break
        if tr==1:
            return reduce(row, 0, iter)
#def reduce(A, M, N, lg, BG):
#    lenght=512-512%len(BG)
#    B=numpy.zeros((lenght, 512), dtype='i')
#    for iter in range(0,512)
#        for iter1 in range(0, lenght)
#            B
