import random

def find_k(network,k,heuristic):
    found = list()
    for _ in range(k):
        pos = random.choice(list(network.keys()))
        res = hill_climbing(network,pos,found,heuristic)
        if (res!=-1):
            found.append(res)
        else:
            print("deu erro, jesus")

    menor = float('inf')
    v_menor = -1
    for x in range(len(found)):
        if (heuristic(network[found[x]]) < menor):
            menor = heuristic(network[found[x]])
            v_menor = x
    for _ in range(2*k):
        pos = random.choice(list(network.keys()))
        res = hill_climbing(network,pos,found,heuristic,mini=menor)
        if (heuristic(network[res])>menor):
            found.pop(v_menor)
            found.append(res)
            menor = float('inf')
            for x in range(len(found)):
                if (heuristic(network[found[x]]) < menor):
                    menor = heuristic(network[found[x]])
                    v_menor = x
    return found

def hill_climbing(network,pos,found,heuristic,mini=0,depth=0):
    node = network[pos]
    n_max = heuristic(node)
    id_max = pos

    for x in range(len(node[0])):
        n_node = network[node[0][x]]
        h_node = heuristic(n_node)
        if ((h_node > n_max) and (node[0][x] not in found) and (h_node > mini)):
            n_max = h_node
            id_max = node[0][x]

    if (depth==10):
        return id_max

    if (id_max!=pos):
        return hill_climbing(network,id_max,found,heuristic)

    return pos