def getInteractions(len):
    interactions = []
    for i in range(len-1):
        for j in range(i+1,len):
            interactions.append((i,j))
    return interactions
    