#coding: utf-8
import pickle

'''
A base de dados consiste em 4 grafos: social(quem segue quem), menções, retweets e respostas. O grafo principal do
trabalho será o de  seguidores e os outros serão utilizados para coletar informações que serão utilizadas no cálculo
das heurísticas.
Cada nó terá os seguintes atributos:
    • Lista de quem ele segue
    • Lista de seguidores
    • Quantidade de pessoas que o mencionaram e são seus seguidores
    • Quantidade de pessoas que o mencionaram, mas não são seus seguidores
    • Quantidade total de menções
    • Quantidade de retweets de seguidores
    • Quantidade de retweets de não seguidores
    • Quantidade de respostas de seguidores
    • Quantidade de respostas de não seguidores
    • Quantidade de pessoas que o responderam e são seus seguidores
    • Quantidade de pessoas que o responderam, mas não são seus seguidores
Formato do nó: network[nó] = [[], [], 0,0,0,0,0,0,0,0,0]
'''

arq = open("higgs-social_network.edgelist", 'r')
network = {}
edges = arq.readlines()
total = len(edges)
i = 0
for line in edges:
    if i%10000 == 0:
        print "SOCIAL: {} de {}".format(i, total)
    i += 1
    a, b = map(int, line.split())
    if a not in network:
        network[a] = [[], [], 0,0,0,0,0,0,0,0,0]
    if b not in network:
        network[b] = [[], [], 0,0,0,0,0,0,0,0,0]
    network[a][0].append(b)
    network[b][1].append(a)
arq.close()

arq = open("higgs-mention_network.edgelist", 'r')
edges = arq.readlines()
total = len(edges)
i = 0
for line in edges:
    if i%10000 == 0:
        print "MENTION: {} de {}".format(i, total)
    i += 1
    a,b,qt = map(int, line.split())
    if a in network[b][1]:
        network[b][2] += 1
    else:
        network[b][3] += 1
    network[b][4] += qt
arq.close()

arq = open("higgs-retweet_network.edgelist", 'r')
edges = arq.readlines()
total = len(edges)
i = 0
for line in edges:
    if i%10000 == 0:
        print "RETWEET: {} de {}".format(i, total)
    i += 1
    a,b,qt = map(int, line.split())
    if a in network[b][1]:
        network[b][5] += qt
    else:
        network[b][6] += qt
arq.close()

arq = open("higgs-reply_network.edgelist", 'r')
edges = arq.readlines()
total = len(edges)
i = 0
for line in edges:
    if i%10000 == 0:
        print "REPLY: {} de {}".format(i, total)
    i += 1
    a,b,qt = map(int, line.split())
    if a in network[b][1]:
        network[b][7] += qt
        network[b][9] += 1
    else:
        network[b][8] += qt
        network[b][10] += 1
arq.close()

pickle.dump(network, open("network.graph", 'wb'))