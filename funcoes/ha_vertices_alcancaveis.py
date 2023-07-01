from classes.grafo import Grafo

def dfs(grafo, vertice, visitados, vertices_alcancaveis):
    visitados.add(vertice)
    vertices_alcancaveis.append(vertice)
    for aresta in grafo.arestas:
        if vertice in aresta:
            vizinho = aresta[0] if aresta[0] != vertice else aresta[1]
            if vizinho not in visitados:
                dfs(grafo, vizinho, visitados, vertices_alcancaveis)

def haVerticesAlcancaveis(grafos: list[Grafo], verticeInicial):
    haVerticesAlcancaveis = []

    for grafo in grafos:
        visitados = set()
        vertices_alcancaveis = []
        dfs(grafo, verticeInicial, visitados, vertices_alcancaveis)
        haVerticesAlcancaveis.append(vertices_alcancaveis)
    
    return haVerticesAlcancaveis


        

        