def heuristic1(node):
    return len(node[1]) * 0.4 + \
           (node[5] + node[6]) * 0.3 + \
           (node[7] + node[8]) * 0.1 + \
           node[4] * 0.2


def heuristic2(node):
    return 0.6 * (node[3] + node[7] + node[11] + 0.35 * node[5] + 0.5 * node[9] + 0.25 * node[13]) + \
           0.4 * (node[2] + node[6] + node[10] + 0.35 * node[4] + 0.5 * node[8] + 0.25 * node[12])
