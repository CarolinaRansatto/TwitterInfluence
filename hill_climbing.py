import random


def influence(node):
    return len(node[1])


def hill_climbing(network):
    pos = [random.choice(list(network.keys()))]
    global nid

    while pos:
        print(pos)
        nid, node = pos[0], network[pos[0]]
        inf = influence(node)
        pos = node[0]
        for i in pos:
            if influence(network[i]) <= inf:
                pos.remove(i)

    return nid
