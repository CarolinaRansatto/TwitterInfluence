import random

def find_k(network,k,heuristic):        #funcao base para a busca utilizando a heuristica
    found = list()         #lista de elementos ja encontrados na busca
    for _ in range(k):     #itera k vezes
        pos = random.choice(list(network.keys()))        #acha um valor aleatorio nas chaves do dicionario que o grafo esta contido
        res = hill_climbing(network,pos,found,heuristic)      #chama a funcao de busca passando esse valor aleatorio como ponto de partida e a lista de nos ja encontrados
        if (res!=-1):         #evita eventuais erros
            found.append(res)    #adiciona o novo resultado a lista de elementos ja encontrados
        else:     #caso exista um erro inesperado
            print("deu erro, jesus")

    #procura o menor valor de heuristica em toda a lista de elementos ja encontrados
    menor = float('inf')      #inicializa a variavel menor com o maximo valor possivel
    v_menor = -1     #indice na lista do menor valor encontrado 
    for x in range(len(found)):     #itera sobre todos os valores encontrados
        if (heuristic(network[found[x]]) < menor):   #caso encontre um valor menor que a variavel menor altera o status das variaveis acima
            menor = heuristic(network[found[x]])
            v_menor = x

    #tendo os nos encontrados acima repetimos o processo abaixo 2k vezes
    for _ in range(2*k):
        pos = random.choice(list(network.keys()))   #escolhemos novamente um valor aleatorio nas chaves 
        res = hill_climbing(network,pos,found,heuristic,mini=menor)     #chama novamente a funcao de busca so que com
        #uma principal alteracao, adicionamos um valor minimo a ser retornado, que e o menor valor de heuristica presente na lista
        #atual de nos influentes
        
        if (heuristic(network[res])>menor):   #somente altera o valor na lista caso seja retornado um valor melhor
            found.pop(v_menor)  #retira o valor antigo
            found.append(res)  #insere o novo valor
            
            menor = float('inf')  #procura novamente o menor valor de heuristica na lista
            for x in range(len(found)):
                if (heuristic(network[found[x]]) < menor):
                    menor = heuristic(network[found[x]])
                    v_menor = x
    return found    #retorna a lista dos k nos influentes

def hill_climbing(network,pos,found,heuristic,mini=0):   #funcao que encontra o maior valor de heuristica a partir de um ponto especifico
    node = network[pos]   #referencia ao no do valor passado como paramentro
    n_max = heuristic(node)    #variavel do maior valor de heuristica atual
    id_max = pos     #id do maior valor de heuristica

    for x in range(len(node[0])):    #visita todos os nos seguidos pelo no atual (vizinhos)
        n_node = network[node[0][x]]    #referencia ao no do vizinho atual
        h_node = heuristic(n_node)    #valor da heuristica do no vizinho atual
        if ((h_node > n_max) and (node[0][x] not in found) and (h_node > mini)):     #caso a heuristica do novo no seja maior que a do antigo 
        #e o no vizinho nao esteja nos valores encontrados e ele seja maior que o valor minimo (mini tem valores 0 nas primeiras k execucoes)
        #o novo no maior se torna esse filho
            n_max = h_node
            id_max = node[0][x]

    if (id_max!=pos):     #se o meu maior no for um dos vizinhos
        return hill_climbing(network,id_max,found,heuristic,mini)

    return pos   #retorna somente se meu maior no for o meu no atual