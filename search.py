

def search(network,nodes,k):
    influence = []
    for n in nodes:
        influence.append(count_influence(network,n,k))
    return influence


def count_influence(network,key,limit):
    vis = ini_hash()
    t_do = list()
    t_do.append((key,0))
    cont = -1
    while(len(t_do)!=0):
        ind = t_do.pop(0)
        if (search_hash(vis,ind[0])):
            ins_hash(vis,ind[0])
            print(ind[0])
            cont += 1
            #if (cont%1000==0):
                #print(cont)
            node = network[ind[0]]
            dep = ind[1]
            if (dep < limit):
                for x in range(len(node[1])):
                    if (search_hash(vis,node[1][x])):
                        t_do.append((node[1][x],dep+1))
    return cont

def ini_hash():
    l = list()
    for _ in range(1000):
        l.append([])
    return l

def ins_hash(h,val):
    pos = val%1000
    h[pos].append(val)

def search_hash(h,val):
    pos = val%1000
    if (val in h[pos]):
        return False
    return True


