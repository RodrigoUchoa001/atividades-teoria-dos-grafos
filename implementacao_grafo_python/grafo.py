class Grafo: 
    def __init__(self, matriz):
        self.matriz = matriz
    
    # se pelo menos uma posicao da matriz for maior q 1, quer dizer q tem mais de uma
    # aresta entre aquele par de vértices, então é multigrafo
    def eMultigrafo(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if (self.matriz[i][j]>1):
                    return True
        
        return False
    
    # se houver laço, é pseudografo
    # isso pode ser verificado vendo se um vértice incide nele msm, essa info fica 
    # na diagonal principal 
    def ePseudografo(self):
        for i in range(len(self.matriz)):
            if (self.matriz[i][i]>0):
                return True
        
        return False

grafo1 = Grafo([
            [0,2,1,0],
            [2,1,1,0],
            [1,1,0,3],
            [0,0,3,0],
        ]
    )

print(grafo1.ePseudografo())
