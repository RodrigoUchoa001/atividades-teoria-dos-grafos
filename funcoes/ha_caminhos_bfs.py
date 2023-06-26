from classes.grafo import Grafo

from collections import deque

def ha_caminhos_bfs(grafos: list[Grafo], partida, chegada):
    haCaminho: list[Grafo] = []
    
    for grafo in grafos:
        caminho = bfs(grafo, partida, chegada)

        if caminho:
            haCaminho.append((grafo.id, caminho))

    return haCaminho


def bfs(grafo: Grafo, start, end):
    # Verificar se os vértices de início e fim estão no grafo
    if start not in grafo.vertices or end not in grafo.vertices:
        return None

    # Criar uma fila para armazenar os vértices a serem visitados
    queue = deque()

    # Criar um dicionário para rastrear os predecessores de cada vértice visitado
    predecessors = {}

    # Iniciar a busca em largura a partir do vértice de início
    queue.append(start)
    predecessors[start] = None

    while queue:
        current_vertex = queue.popleft()

        # Verificar se chegamos ao vértice de destino
        if current_vertex == end:
            break

        # Encontrar os vizinhos do vértice atual
        neighbors = [edge[1] for edge in grafo.arestas if edge[0] == current_vertex]

        # Adicionar os vizinhos não visitados à fila
        for neighbor in neighbors:
            if neighbor not in predecessors:
                queue.append(neighbor)
                predecessors[neighbor] = current_vertex

    # Construir o caminho a partir dos predecessores
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        if current_vertex not in predecessors:
            break
        current_vertex = predecessors[current_vertex]

    if current_vertex is None:
        # Inversão do caminho para obter a ordem correta
        path.reverse()
        # Retornar o caminho encontrado
        return path
    else:
        # Não há caminho entre os vértices de início e fim
        return None
        