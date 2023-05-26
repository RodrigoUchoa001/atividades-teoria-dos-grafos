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


#exemplo 1 - testando grafo simples (grafo da livro 1.2 a) - pág 13)
grafoSimples = Grafo([
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)

print('grafo simples é multigrafo:', grafoSimples.eMultigrafo())
print('grafo simples é pseudografo:', grafoSimples.ePseudografo())

# exemplo 2 - testando multigrafo (grafo da livro 1.2 b) - pág 13)
grafoMultigrafo = Grafo([
        [0, 2, 1, 0],
        [2, 0, 1, 0],
        [1, 1, 0, 3],
        [0, 0, 3, 0],
    ]
)

print('grafo multigrafo é multigrafo:', grafoMultigrafo.eMultigrafo())
print('grafo multigrafo é pseudografo:', grafoMultigrafo.ePseudografo())


# exemplo 3 - testando pseudografo (pequena alteração no grafo anterior)
grafoPseudografo = Grafo([
        [0, 2, 1, 0],
        [2, 1, 1, 0],
        [1, 1, 0, 3],
        [0, 0, 3, 0],
    ]
)

print('grafo pseudografo é multigrafo:', grafoPseudografo.eMultigrafo())
print('grafo pseudografo é pseudografo:', grafoPseudografo.ePseudografo())


# exemplo 4 - testando digrafo simples (grafo da livro 1.4 a) - pág 16)
digrafoSimples = Grafo([
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
    ]
)

print('digrafo simples é multigrafo:', digrafoSimples.eMultigrafo())
print('digrafo simples é pseudografo:', digrafoSimples.ePseudografo())

# exemplo 5 - testando pseudografo direcionado (grafo da livro 1.4 b) - pág 16)
pseudografoDirecionado = Grafo([
        [0, 2, 0, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 2],
        [0, 0, 1, 0],
    ]
)

print('pseudografo direcionado é multigrafo:', pseudografoDirecionado.eMultigrafo())
print('pseudografo direcionado é pseudografo:', pseudografoDirecionado.ePseudografo())