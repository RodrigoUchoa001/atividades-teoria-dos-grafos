import json

class Grafo:
    def __init__(self, id, vertices, arestas):
        self.id = id
        self.vertices = vertices
        self.arestas = arestas

# TODO: colocar pra ler de um arquivo passado por parametro no terminal
file = open('c:/Users/franr/Documents/uespi/periodo 7/teoria dos grafos/atividades-teoria-dos-grafos/implementacao_modelo_do_alcemir/graphs.json')
dados = json.load(file)

grafos = []
# aqui vou ter uma lista com todos os grafos em forma de objeto
for i in  dados['graphs']:
    grafos.append(
        Grafo(
            i['id'],
            i['vertices'],
            i['edges'],
        )
    )
