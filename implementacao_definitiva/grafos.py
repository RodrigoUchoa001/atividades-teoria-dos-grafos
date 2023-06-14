import json
from classes.grafo import Grafo

from funcoes.sao_multigrafos import saoMultigrafos
from funcoes.sao_pseudografos import saoPseudografos
from funcoes.grau import grauDeVerticeEspecifico

# TODO: colocar pra ler de um arquivo passado por parametro no terminal
file = open('c:/Users/franr/Documents/uespi/periodo 7/teoria dos grafos/atividades-teoria-dos-grafos/implementacao_definitiva/graphs.json')
dados = json.load(file)

grafos: list[Grafo] = []
# aqui vou ter uma lista com todos os grafos em forma de objeto
for i in dados['graphs']:
    grafos.append(
        Grafo(
            i['id'],
            i['vertices'],
            i['edges'],
        )
    )

print("carregado", len(grafos), "grafos")

# for i in range(len(grafos)):
#     print(grafos[i].vertices)

# testando multigrafos
# saoPseudografos(grafos)

# testando grau de vértice especifico
grauDeVerticeEspecifico(grafos[0], "B")
