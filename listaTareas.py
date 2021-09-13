class Nodo:
    def __init__(self,datos):
        self.datos=datos
        self.next=None
        self.previous=None

class ListaTareas:
    def __init__(self):
        self.head=None
        self.body=None

    def insertar(self,datos):
        nuevo=Nodo(datos)
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
                print(nodo.datos)
                nodo=nodo.next
        
    def mostrarI(self):
        nodo=self.body
        if self.head!=None:
            while(nodo):
                print(nodo.datos)
                nodo=nodo.previous