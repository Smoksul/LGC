def put(BG, GL):
    vec = ""
    wid = 500
    widB = len(BG)
    widG = len(GL)
    res=""
    k = ((wid-(wid%2))/2) - ((len(GL) - (len(GL)%2)))/2
    chk=1
    for iter in range(0, k):
        res=res+BG[iter%widB]
    k=k-widB
    while chk:
        for iter in range(0, widB):
            if res[k+iter]==GL[iter]:
                chk=0
            else:
                k=k-1
                chk=1
                break
    k+widB
    temp=""
    for iter in range(0, k):
        temp=temp+res[iter]
    res=temp
    for iter in range(0, widG):
        res=res+GL[iter]
    k=k+widG
    chk=1
    while chk:
        for iter in range(0, widB):
            if res[k-iter-1]==BG[widB-iter-1]:
                chk=0
            else:
                k=k-1
                chk=1
                break
    temp=""
    for iter in range(0, k):
        temp=temp+res[iter]
    res=temp
    for iter in range(0, wid-k):
        res=res+BG[iter%widB]
    return res
