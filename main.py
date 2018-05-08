from network import load_network, create_graph
from heuristics import heuristic1, heuristic2
from hill_climbing import hill_climbing,find_k
from search import search

print("Aguarde enquanto os dados sao carregados na memoria...")

try:
    network = load_network()
except FileNotFoundError:
    create_graph()
    network = load_network()

k = int(input("Digite o valor k (total de nos influentes): "))
print()

print("Resultados da busca com H1:\n")
l = find_k(network, k, heuristic1)
for x in range(len(l)):
    print("{} com valor: {}".format(l[x], heuristic1(network[l[x]])))
print()
print(search(network,l,2))

print("Resultados da busca com H2:\n")
l = find_k(network, k, heuristic2)
for x in range(len(l)):
    print("{} com valor: {}".format(l[x], heuristic2(network[l[x]]))) 

print(search(network,l,2))
