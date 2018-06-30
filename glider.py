def put(BG, GL):
    vec = ""
    wid = 1500 - (1500%len(BG))
    widB = wid/len(BG)
    for i in range(0, widB):
        vec += BG

    k = wid - ((len(GL) - (len(GL)%2)))/2
    widG = len(GL)
    for i in range(0, widG):
        vec[k] = GL[i]
        k+=1
    return vec
    
