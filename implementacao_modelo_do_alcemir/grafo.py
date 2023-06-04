class Grafo:
    def __init__(self, id, vertices, arestas):
        self.id = id
        self.vertices: list = vertices
        self.arestas: list = arestas

# class OperacoesGrafo:
#     def __init__(self, grafos :list[Grafo]):
#         self.grafos = grafos
        
def saoMultigrafos(grafos:list[Grafo]):
    saoMultigrafos: list[bool] = [0 for _ in range(len(grafos))]

    for i in range(len(grafos)):
        arestasRepetidas = []
        

