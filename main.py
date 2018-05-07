from network import load_network, create_graph
from heuristics import heuristic1, heuristic2
from hill_climbing import hill_climbing,find_k
from search import search

try:
    network = load_network()
except FileNotFoundError:
    create_graph()
    network = load_network()

l = find_k(network, 10, heuristic1)
for x in range(len(l)):
    print("{} com valor: {}".format(l[x], heuristic1(network[l[x]])))

print(search(network,l,2))
