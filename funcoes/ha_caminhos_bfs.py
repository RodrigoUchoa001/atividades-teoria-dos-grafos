from classes.grafo import Grafo

from collections import deque

def haCaminhoBfs(grafos: list[Grafo], partida, chegada):
    haCaminho: list[Grafo] = []
    
    for grafo in grafos:
        caminho = bfs(grafo, partida, chegada)

        if caminho:
            haCaminho.append((grafo.id, caminho))
        else:
            haCaminho.append((grafo.id, "caminho não encontrado"))

    return haCaminho

def bfs(grafo: Grafo, partida, chegada):
    fila = deque([(partida, [partida])])
    visitados = set()

    while fila:
        verticeAtual, caminhoAtual = fila.popleft()

        if verticeAtual == chegada:
            return caminhoAtual

        visitados.add(verticeAtual)

        for aresta in grafo.arestas:
            if verticeAtual in aresta:
                vizinho = aresta[0] if aresta[0] != verticeAtual else aresta[1]
                if vizinho not in visitados:
                    fila.append((vizinho, caminhoAtual + [vizinho]))
    return None