def search(network, nodes):
    influence = []
    for n in nodes:
        influence.append(count_influence(network, network[n]))
    return influence


def count_influence(network, node, influencee=[], depth=0):
    if depth == 2:
        return
    for follower in node[1]:
        if follower not in influencee:
            influencee.append(follower)
            count_influence(network, network[follower], influencee, depth + 1)
    return influencee
