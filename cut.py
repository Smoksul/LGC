def cut(rlchoice, linechoice):
    fname="../out/out_"+str(rlchoice)+".dat"
    file=open(fname)
    return file.readline(linechoice)