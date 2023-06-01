import json
import grafo

# TODO: colocar pra ler de um arquivo passado por parametro no terminal
file = open('c:/Users/franr/Documents/uespi/periodo 7/teoria dos grafos/atividades-teoria-dos-grafos/implementacao_modelo_do_alcemir/graphs.json')
dados = json.load(file)

grafos: list[grafo.Grafo] = []
# aqui vou ter uma lista com todos os grafos em forma de objeto
for i in dados['graphs']:
    grafos.append(
        grafo.Grafo(
            i['id'],
            i['vertices'],
            i['edges'],
        )
    )

# for i in range(len(grafos)):
#     print(grafos[i].vertices)
