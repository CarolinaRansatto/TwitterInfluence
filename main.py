from network import load_network
from heuristics import heuristic1, heuristic2
from hill_climbing import hill_climbing

network = load_network()
nid = hill_climbing(network, heuristic1)

print(len(network))

print('{}: {}'.format(nid, network[nid]))
