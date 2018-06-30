def cut(rlchoice, linechoice):
    fname="../out/out_"+str(rlchoice)+".dat"
    file=open(fname)
    line=file.readline(linechoice)
    refline=""
    for iter in range(0, len(line)):
        if line[iter]!=' ':
            refline=refline+line[iter]
    return refline