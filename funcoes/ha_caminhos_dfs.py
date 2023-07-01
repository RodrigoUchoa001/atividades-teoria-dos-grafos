from classes.grafo import Grafo

def haCaminhoDfs(grafos: list[Grafo], partida, chegada):
    haCaminho: list[Grafo] = []
    
    for grafo in grafos:
        caminho = dfs(grafo, partida, chegada, [], set())

        if caminho:
            haCaminho.append((grafo.id, caminho))
        else:
            haCaminho.append((grafo.id, "caminho não encontrado"))

    return haCaminho

def dfs(grafo, verticeAtual, verticeDestino, caminhoAtual, visitados):
    if verticeAtual == verticeDestino:
        caminhoAtual.append(verticeAtual)
        return caminhoAtual

    visitados.add(verticeAtual)

    for aresta in grafo.arestas:
        if verticeAtual in aresta:
            vizinho = aresta[0] if aresta[0] != verticeAtual else aresta[1]
            if vizinho not in visitados:
                caminhoEncontrado = dfs(grafo, vizinho, verticeDestino, caminhoAtual + [verticeAtual], visitados)
                if caminhoEncontrado:
                    return caminhoEncontrado

    return None