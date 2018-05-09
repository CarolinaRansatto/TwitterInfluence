from network import load_network, create_graph
from heuristics import heuristic1, heuristic2
from hill_climbing import hill_climbing,find_k
from search import search

print("Aguarde enquanto os dados sao carregados na memoria...")

#Carrega o grafo na memoria caso o grafo ja exista e cria o grafo a partir dos arquivos originais caso ele
#nao seja encontrado
try:
    network = load_network()
except FileNotFoundError:
    create_graph()
    network = load_network()

k = int(input("Digite o valor k (total de nos influentes): "))


print("Procurando os k mais influentes com a heuristica 1...")
l = find_k(network, k, heuristic1)     #chama a função para a descoberta dos k nos usando a heuristica 1
print("K mais influentes encontrados.\nVerificando a popularidade dos k nos...")
r = search(network,l,2)    #busca exata para validar a popularidade dos k obtidos atraves da busca acima
print("Resultados da busca com H1:\n")
for x in range(len(l)):
    print("{} com valor de heuristica: {:.2f} e alcance de popularidade: {}".format(l[x], heuristic1(network[l[x]]),r[x]))
print()


print("Procurando os k mais influentes com a heuristica 2...")
l = find_k(network, k, heuristic2)    #chama a função para a descoberta dos k nos usando a heuristica 2
print("K mais influentes encontrados.\nVerificando a popularidade dos k nos...")
r = search(network,l,2)        #busca exata para validar a popularidade dos k obtidos atraves da busca acima
print("Resultados da busca com H2:\n")
for x in range(len(l)):
    print("{} com valor de heuristica: {:.2f} e alcance de popularidade: {}".format(l[x], heuristic2(network[l[x]]),r[x])) 
