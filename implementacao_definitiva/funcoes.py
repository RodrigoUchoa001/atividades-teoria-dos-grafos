import grafo    

def saoMultigrafos(grafos: list[grafo.Grafo]):
    saoMultigrafos: list[grafo.Grafo] = []

    for grafo in grafos:
        
        for i in range(len(grafo.matrizADJ)):
            for j in range(len(grafo.matrizADJ[i])):

                if (grafo.matrizADJ[i][j]>1):
                    saoMultigrafos.append(grafo)
                    break
        
    print("dentre esses grafos, são multigrafos os com os seguintes IDs:") 
    for grafo in saoMultigrafos:
        print(grafo.id)

def saoPseudografos(grafos: list[grafo.Grafo]):
    saoPseudografos: list[grafo.Grafo] = []

    for grafo in grafos:

        for i in range(len(grafo.matrizADJ)):
            if (grafo.matrizADJ[i][i]>0):
                    saoPseudografos.append(grafo)
                    break
        
    print("dentre esses grafos, são pseudgrafos os com os seguintes IDs:") 
    for grafo in saoPseudografos:
        print(grafo.id)


