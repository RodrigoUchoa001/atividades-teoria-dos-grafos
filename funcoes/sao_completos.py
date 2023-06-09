from classes.grafo import Grafo

def saoCompletos(grafos: list[Grafo]):
    saoCompletos: list[Grafo] = []

    for grafo in grafos:
        vertices = grafo.vertices
        arestas = grafo.arestas

        # Verificar se o número de arestas é igual ao número máximo possível de arestas
        # formula pra saber se um grafo é completo, tendo 'n' vértices:
        # n * (n - 1) / 2
        if len(arestas) == len(vertices) * (len(vertices) - 1) // 2:
            saoCompletos.append(grafo)  # O grafo é completo
    
    return saoCompletos
