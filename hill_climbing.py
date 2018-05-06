import random


def hill_climbing(network, heuristic):
    pos = [random.choice(list(network.keys()))]
    global nid

    while pos:
        print(pos)
        nid, node = pos[0], network[pos[0]]
        inf = heuristic(node)
        pos = node[0]
        for i in pos:
            if heuristic(network[i]) <= inf:
                pos.remove(i)

    return nid
