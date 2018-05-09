def search(network,nodes,k):     #busca que valida a popularidade dos nos encontrados pela outra busca
    influence = []      #lista do total de nos influenciados
    for n in nodes:
        print("Verificando popularidade do no {}...".format(n))
        influence.append(count_influence(network,n,k))     #adiciona na lista os valores retornados pela busca exata
    return influence     #retorna a lista


def count_influence(network,key,limit):      #busca por largura que valida os nos populares
    reboot_vis(network)     #reseta o campo visitado dos nos da base
    t_do = list()     #lista de nos a serem visitados que e vista como uma fila
    t_do.append((key,0))    #adiciona a lista de nos o no popular e sua profundidade atual
    cont = -1     #contador que representa a quantidade de nos influenciados
    while(len(t_do)!=0):     #enquanto existirem nos a serem visitados
        ind = t_do.pop(0)     #retira da fila o proximo no a ser visitado
        cont += 1     #adiciona ao contador de influencia
        node = network[ind[0]]      #referencia ao no atual
        dep = ind[1]      #profundidade do no atual
        if (dep < limit):   #limita a busca a uma profundidade igual a limit
            for x in range(len(node[1])):    #itera sobre os seguidores do no atual
                n_node = network[node[1][x]]      #referencia ao no do seguidor
                if (int(n_node[14]) == int(0)):      #caso o no ainda n tenha sido adicionado a fila ou visitado
                    n_node[14] = 1    #tira a possibilidade de outra adicao do no a fila
                    t_do.append((node[1][x],dep+1))       #adiciona o no a fila
    return cont     #retorna o contador de influencia

def reboot_vis(l):      #funcao que reseta a posicao visitado dos nos
    for key in l:
        l[key][14] = 0
