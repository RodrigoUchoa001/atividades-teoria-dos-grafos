void main() {
  Grafo grafo = Grafo(
    [
      Vertice('1'),
      Vertice('2'),
      Vertice('3'),
      Vertice('4'),
      Vertice('5'),
    ],
    [
      Aresta('1','2'),
      Aresta('2','3'),
      Aresta('3','4'),
      Aresta('5','1'),
//       Aresta('5','6'),
    ]
  );
  
  grafo.printaArestas();
}


class Grafo{
  List<Vertice> vertices = [];
  List<Aresta> arestas = [];
  
  Grafo(List<Vertice> vertices, List<Aresta> arestas){
    if(!testaArestas(arestas)){
      throw 'vértices das arestas n existem';
    }
    this.arestas = arestas;
  }
  
  bool testaArestas(List<Aresta> arestas){
    arestas.map((aresta) {
      },
    );
    return true;   
  }
  
  void printaArestas(){    
    print('${arestas.length} arestas');
    for(int i=0; i<arestas.length; i++){
      print('{${arestas[i].vertice1}, ${arestas[i].vertice2}}');
    }
  }      
}

class Vertice{
  String nome;
  
  Vertice(this.nome);
}

class Aresta{
  final String vertice1;
  final String vertice2;
  
  const Aresta(this.vertice1, this.vertice2);
}
