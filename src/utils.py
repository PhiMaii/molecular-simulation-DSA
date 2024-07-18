def lennardJones(part1, part2):
    r = part1.pos-part2.pos

#this functions generates a list of tuples referring to every interaction between all elements of a list -> e.g list with three elements -> [(0,1),(0,2),(1,2)]
def getInteractions(len):
    tups = []
    for i in range(len-1):
        for j in range(i+1,len):
            tup = (i,j)
            tups.append((i,j))
    return tups