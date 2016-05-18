import simmeasures

def wellsep:
    #recebe uma lista com os clusters já prontos
    #separa em k listas(dependendo da quantidade de clusters)
    #calcula a distancia de um ponto pra todos dentro do mesmo cluster
    #pega o ponto com a maior distancia dentro do cluster, vai ser o parametro de comparacao
    #começa a comparar com pontos de outros clusters
    #Se algum ponto de outro cluster for mais proximo que o parametro intracluster, retorna dizendo que não é wellsep
    #Se não, passa para o proximo ponto do primeiro cluster
    #Se todos os pontos forem comparados e a distancia intracluster sempre for menor, então é wellsep


def centbased:
    #recebe uma lista com os clusters já prontos
    #separa em k listas(dependendo da quantidade de clusters)
    #Calcula o centro de cada cluster(media das posições dos pontos)
    #Compara cada ponto com o seu centro e com o centro dos outros clusters
    #Se algum ponto for mais proximo do centro de outro cluster do que do seu proprio, n é centbased
    #Se todos os pontos forem comparados e estiverem assinalados ao centro mais proximo, então é centbased
    
def contg:
    #recebe uma lista com os clusters já prontos
    #separa em k listas(dependendo da quantidade de clusters)
    #calcula a distancia de um ponto pra todos dentro do mesmo cluster
    #pega o ponto com a menor distancia dentro do cluster, vai ser o parametro de comparacao
    #começa a comparar com pontos de outros clusters
    #Se algum ponto de outro cluster for mais proximo que o parametro intracluster, retorna dizendo que não é contg
    #Se não, passa para o proximo ponto do primeiro cluster
    #Se todos os pontos forem comparados e a distancia para o parametro intracluster sempre for menor, então é contg

def densebased:
    #recebe uma lista com os clusters já prontos
    #separa em k listas(dependendo da quantidade de clusters)
    #Calcula o centro de cada cluster(media das posições dos pontos)
    #Compara o centro com o ponto mais distante dentro do cluster, para todos os clusters
    #O raio será o menor valor entre os centros e os pontos mais distantes do cluster
    #calcula a densidade de cada cluster, com base no raio escolhido (salva em uma lista)
    #calcula a distancia entre os centros, e salva o ponto que ficar mais proximo do meio dos dois
    #calcula a densidade na area deste ponto central, com o mesmo raio anterior (feito entre todos os centros, salva em uma lista)
    #Se alguma das densidades fora dos clusters for maior que as densidades dentro dos clusters, não é densebased
    #Se as densidades dentro dos clusters sempre forem maiores, então é densebased

    #ou

    #recebe uma lista com os clusters já prontos
    #separa em k listas(dependendo da quantidade de clusters)
    #Calcula o centro de cada cluster(media das posições dos pontos)
    #Compara o centro com o ponto mais distante dentro do cluster, para todos os clusters
    #O raio será o menor valor entre os centros e os pontos mais distantes do cluster
    #calcula a densidade de cada cluster, com base no raio escolhido (salva em uma lista)
    #calcula a distancia entre os centros, e salva o ponto que ficar mais proximo do meio dos dois
    #calcula a densidade na area deste ponto central, com o mesmo raio anterior
    #Se a densidade nessa area for maior que a densidade de um dos clusters, não é densebased
    #Se não, passa para o proximo par de clusters
    #Se as densidades dentro dos clusters sempre forem maiores, então é densebased
    
