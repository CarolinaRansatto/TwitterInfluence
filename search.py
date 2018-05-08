def search(network,nodes,k):
    influence = []
    for n in nodes:
        influence.append(count_influence(network,n,k))
    return influence


def count_influence(network,key,limit):
    reboot_vis(network)
    t_do = list()
    t_do.append((key,0))
    cont = -1
    while(len(t_do)!=0):
        ind = t_do.pop(0)
        cont += 1
        node = network[ind[0]]
        dep = ind[1]
        if (dep < limit):
            for x in range(len(node[1])):
                n_node = network[node[1][x]]
                if (int(n_node[14]) == int(0)):
                    n_node[14] = 1
                    t_do.append((node[1][x],dep+1))
    return cont

def reboot_vis(l):
    for key in l:
        l[key][14] = 0
