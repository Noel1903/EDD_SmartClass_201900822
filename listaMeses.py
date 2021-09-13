class Nodo:
    def __init__(self,mes):
        self.mes=mes
        self.tareas=None
        self.next=None
        self.previous=None

class ListaMeses:
    def __init__(self):
        self.head=None
        self.body=None

    def insertar(self,mes):
        nuevo=Nodo(mes)
        if self.head==None:
            self.head=nuevo
            self.body=nuevo
        else:
            self.body.next=nuevo
            nuevo.previous=self.body
            self.body=nuevo

    def mostrar(self):
        nodo=self.head
        if self.head!=None:
            while(nodo):
                print(nodo.mes)
                nodo=nodo.next
        
    def mostrarI(self):
        nodo=self.body
        if self.head!=None:
            while(nodo):
                print(nodo.mes)
                nodo=nodo.previous