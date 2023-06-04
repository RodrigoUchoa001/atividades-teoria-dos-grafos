class Grafo:
    def __init__(self, id, vertices, arestas):
        self.id = id
        self.vertices: list = vertices
        self.arestas: list = arestas
        self.criarMatrizDeAdjacencia()

    def criarMatrizDeAdjacencia(self):
        self.matrizADJ = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]

        for aresta in self.arestas:
            origem = self.vertices.index(aresta[0])
            destino = self.vertices.index(aresta[1])
            # self.matrizADJ[origem][destino] = 1 
            self.matrizADJ[origem][destino] = 1 if self.matrizADJ[origem][destino] == 0 else self.matrizADJ[origem][destino]+1

            # self.matrizADJ[destino][origem] = 1 APENAS P/ GRAFO N DIRECIONADO

    
def saoMultigrafos(grafos: list[Grafo]):
    saoMultigrafos: list[Grafo] = []

    for grafo in grafos:
        
        for i in range(len(grafo.matrizADJ)):
            for j in range(len(grafo.matrizADJ[i])):

                if (grafo.matrizADJ[i][j]>1):
                    saoMultigrafos.append(grafo)
                    break
        
    print("dentre esses grafos, são multigrafos os com os seguintes IDs:") 
    for grafo in saoMultigrafos:
        print(grafo.id)

def saoPseudografos(grafos: list[Grafo]):
    saoPseudografos: list[Grafo] = []

    for grafo in grafos:

        for i in range(len(grafo.matrizADJ)):
            if (grafo.matrizADJ[i][i]>0):
                    saoPseudografos.append(grafo)
                    break
        
    print("dentre esses grafos, são pseudgrafos os com os seguintes IDs:") 
    for grafo in saoPseudografos:
        print(grafo.id)