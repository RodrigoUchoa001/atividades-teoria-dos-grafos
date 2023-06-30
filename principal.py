from funcoes.carregar_grafos import carregarGrafos
from funcoes.sao_multigrafos import saoMultigrafos
from funcoes.sao_pseudografos import saoPseudografos
from funcoes.grau import grauDeTodosOsVertices, grauDeVerticeEspecifico

print("FERRAMENTA GRAFOS \nInsira um comando")


class FerramentaGrafos:
    continuarPrograma = True
    grafos = []

    def reconhecerComando(self, comando: str):
        if comando[0] == 'grafos':
            if comando[1] == 'sair':
                print("fim do programa!\n")
                self.continuarPrograma = False
            
            
            elif len(comando) == 3 and comando[1] == 'carregar':
                try:
                    self.grafos = carregarGrafos(comando[2])
                except:
                    print("Arquivo não encontrado!")


            elif comando[1] == 'multigrafos':
                multigrafos = saoMultigrafos(self.grafos)
                print("dentre esses grafos, são multigrafos os com os seguintes IDs:") 
                for grafo in multigrafos:
                    print(grafo.id)
            
            elif comando[1] == 'pseudografos':
                pseudografos = saoPseudografos(self.grafos)
                print("dentre esses grafos, são pseudografos os com os seguintes IDs:") 
                for grafo in pseudografos:
                    print(grafo.id)
            
            elif len(comando) == 3 and comando[1] == 'graus':
                idGrafo = int(comando[2].split('=')[1])

                listaDeGraus = grauDeTodosOsVertices(self.grafos[idGrafo-1])
                print("Esse grafo tem os seguintes graus em cada vértice:")
                for i in range(len(listaDeGraus)):
                    print(self.grafos[idGrafo-1].vertices[i]," - ", listaDeGraus[i])


            
            else:
                print('\nComando não reconhecido, verifique se o comando foi digitado corretamente.')
            
        else:
            print('\nComando não reconhecido, verifique se o comando foi digitado corretamente.')


ferramentaGrafos = FerramentaGrafos()

while ferramentaGrafos.continuarPrograma:
    comando = str(input('\n> '))
    comandoAtual = comando.split()
    ferramentaGrafos.reconhecerComando(comandoAtual)


