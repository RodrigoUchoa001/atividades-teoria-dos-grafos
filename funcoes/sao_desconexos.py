from classes.grafo import Grafo

def dfs(grafo, vertice, visitados):
    visitados.add(vertice)
    for aresta in grafo.arestas:
        if vertice in aresta:
            vizinho = aresta[0] if aresta[0] != vertice else aresta[1]
            if vizinho not in visitados:
                dfs(grafo, vizinho, visitados)

def saoDesconexos(grafos: list[Grafo]):
    saoDesconexos = []

    for grafo in grafos:
        todos_vertices = set(grafo.vertices)
        visitados = set()

        # Encontrar uma raiz (vértice inicial) para iniciar a busca
        raiz = grafo.vertices[0]

        dfs(grafo, raiz, visitados)

        if todos_vertices != visitados:
            saoDesconexos.append(grafo)
    
    return saoDesconexos


