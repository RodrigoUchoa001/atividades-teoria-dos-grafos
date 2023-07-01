from classes.grafo import Grafo
from funcoes.ha_vertices_alcancaveis import haVerticesAlcancaveis


def haVerticesInalcancaveis(grafos: list[Grafo], verticeInicial):
    verticesInalcancaveis = []

    verticesAlcancaveis = haVerticesAlcancaveis(grafos, verticeInicial)

    for i in range(len(verticesAlcancaveis)):
        todosVertices = set(grafos[i].vertices)
        
        verticesInalcancaveisDesseGrafo = todosVertices - set(verticesAlcancaveis[i])
        verticesInalcancaveis.append(verticesInalcancaveisDesseGrafo)
    
    return verticesInalcancaveis