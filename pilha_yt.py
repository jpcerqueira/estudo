#push - inclui um elemento na pilha
#pop - retira um elemento na pilha
#empty - retorna true ou false se a pilha está vazia
#top ou peek - retorna o elemento no topo da pilha
#size - retorna o tamanho da pilha

#para criar uma pilha, tem que ser feito um nó, onde teremos a conexão 'laçada' entre os objetos
#para isso criamos dois objetos, Stack com top/size e o Node com data/next
# Stack apenas irá mostrar o objeto que está no topo da pilha e o tamanho, onde estão os métodos
# Node, onde temos um nó criado, irá ter seus atributos com a data, onde será o valor do objeto e o next, onde será feito o nó com o valor do próxima objeto

class Node:
    def __init__(self, data) -> None: #método construtor
        self.data = data #atributo que será recebido pelo usuário
        self.next = None #todo nó criado será vazio, sem apontar para ninguém, 'possivel atribuição depois'

class Stack: #classe onde terá os métodos que irá ordenar a estrutura pilha
    def __init__(self) -> None: #método construtor
        self.top = None
        self._size = 0

    def push(self, elem): #onde será feito a captação dos dados 
        node = Node(elem) #onde vamos criar o nó para incluir o dado no Node /// criando aqui um objeto depois de feita a instância 
        node.next = self.top
        self.top = node
        self._size += 1

    def pop (self):
        if self.empty():
            return 'Pilha vazia'
        node = self.top
        self.top = self.top.next
        self._size -= 1
        return node.data
    
    def peek (self):
        if self.empty():
            return 'Pilha vazia'   
        return self.top.data   

    def __len__ (self):
        return self._size #coloca o _ do lado do size para demonstrar que é uma variavel interna/local
    
    def empty(self):
        return len(self) == 0
    

#O método __repr__ é semelhante ao método __str__, mas é usado para representar o objeto de forma que possa ser usado para criar um novo objeto com os mesmos valores
    def __repr__(self) -> str: #método representátivo
        if len(self) == 0:
            return 'Pilha vazia'
        s = '' #zera variavel /// s de string, que está zerada
        p = self.top #armazena o topo na variavel p /// p de ponteiro, e está recebendo o self.top pq tem que começar do topo
        while(p): # enquanto o 'p' tiver valor, entra no while qdo tiver valor e sai quando não tiver mais
            s += str(p.data) + '\n' #incrementa informando o data do p
            p = p.next              #aponta para o proximo do p ///  o next = proximo é o prato de baixa da pilha
        return s
    #isso tudo para visualizar a pilha