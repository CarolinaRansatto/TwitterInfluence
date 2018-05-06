from network import load_network, create_graph
from heuristics import heuristic1, heuristic2
from hill_climbing import hill_climbing

try:
    network = load_network()
except FileNotFoundError:
    create_graph()
    network = load_network()

nid = hill_climbing(network, heuristic2)

print('{}: {}'.format(nid, network[nid]))
