from classes.grafo import Grafo

def grauDeVerticeEspecifico(grafo: Grafo, vertice):
    grau = 0
    for i in range(len(grafo.arestas)):
        if grafo.arestas[i][0] == vertice or grafo.arestas[i][1] == vertice:
            grau = grau + 1
    print("o grau do vértice ",vertice," é ",grau)
