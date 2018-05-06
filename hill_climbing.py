import random

def find_k(network,k,heuristic):
    found = list()
    for _ in range(k):
        pos = [random.choice(list(network.keys()))]
        res = hill_climbing(network,pos[0],found,heuristic,0)
        if (res!=-1):
            found.append(res)
        else:
            print("deu erro, jesus")
    return found

def hill_climbing(network,pos,found,heuristic,depth):
    if (depth == 0):
        n_id,node = pos,network[pos]
        cur = heuristic(node)
        id_max = -1
        for x in range(len(node[0])):
            n_node = network[node[0][x]]
            h_node = heuristic(n_node)
            if ((h_node >= cur) and (node[0][x] not in found)):
                n_max = h_node
                id_max = x
        if (id_max!=-1):
            return hill_climbing(network,node[0][id_max],found,heuristic,depth)
        return pos
    else:
        pass