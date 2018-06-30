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
