import pickle

'''
A base de dados consiste em 4 grafos: social(quem segue quem), menções, retweets e respostas. O grafo principal do
trabalho será o de  seguidores e os outros serão utilizados para coletar informações que serão utilizadas no cálculo
das heurísticas.
Cada nó terá os seguintes atributos:
    [0] Lista de quem ele segue
    [1] Lista de seguidores
    [2] Quantidade de menções de seguidores
    [3] Quantidade de menções de não seguidores
    [4] Quantidade de pessoas que o mencionaram e são seus seguidores
    [5] Quantidade de pessoas que o mencionaram, mas não são seus seguidores
    [6] Quantidade de retweets de seguidores
    [7] Quantidade de retweets de não seguidores
    [8] Quantidade de pessoas que o retweetaram e são seus seguidores
    [9] Quantidade de pessoas que o retweetaram, mas não são seus seguidores
    [10] Quantidade de respostas de seguidores
    [11] Quantidade de respostas de não seguidores
    [12] Quantidade de pessoas que o responderam e são seus seguidores
    [13] Quantidade de pessoas que o responderam, mas não são seus seguidores
Formato do nó: network[nó] = [[], [], 0,0,0,0,0,0,0,0,0]
'''


def load_network():
    return pickle.load(open('files/network.graph', 'rb'))


def create_graph():
    arq = open("files/higgs-social_network.edgelist", 'r')
    network = {}
    edges = arq.readlines()
    for line in edges:
        a, b = map(int, line.split())
        if a not in network:
            network[a] = [[], [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if b not in network:
            network[b] = [[], [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        network[a][0].append(b)
        network[b][1].append(a)
    arq.close()

    arq = open("files/higgs-mention_network.edgelist", 'r')
    edges = arq.readlines()
    for line in edges:
        a, b, qt = map(int, line.split())
        if a in network[b][1]:
            network[b][2] += qt
            network[b][4] += 1
        else:
            network[b][3] += qt
            network[b][5] += 1
    arq.close()

    arq = open("files/higgs-retweet_network.edgelist", 'r')
    edges = arq.readlines()
    for line in edges:
        a, b, qt = map(int, line.split())
        if a in network[b][1]:
            network[b][6] += qt
            network[b][8] += 1
        else:
            network[b][7] += qt
            network[b][9] += 1
    arq.close()

    arq = open("files/higgs-reply_network.edgelist", 'r')
    edges = arq.readlines()
    for line in edges:
        a, b, qt = map(int, line.split())
        if a in network[b][1]:
            network[b][10] += qt
            network[b][12] += 1
        else:
            network[b][11] += qt
            network[b][13] += 1
    arq.close()

    pickle.dump(network, open("files/network.graph", 'wb'))
