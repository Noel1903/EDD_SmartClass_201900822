class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.puntero=None
        self.next=None
        self.previous=None

class ListaDatos:
    def __init__(self):
        self.head=None
        self.body=None
    def insertar(self,dato):
        nuevo=Nodo(dato)
        if self.head==None:
            self.head=nuevo
            self.body=nuevo
           
        else:
            if dato<self.head.dato:
                nuevo.next=self.head
                self.head.previous=nuevo
                self.head=nuevo
                
            elif dato>self.body.dato:
                self.body.next=nuevo
                nuevo.previous=self.body
                self.body=nuevo
                
            else:
                nodo=self.head
                while nodo:
                    if nodo.dato<dato and nodo.next.dato>dato:
                        nodo.next.previous=nuevo
                        nuevo.next=nodo.next
                        nodo.next=nuevo
                        nuevo.previous=nodo
                        break
                    nodo=nodo.next

    def existe(self,dato):
        existe=False
        if self.head==None:
            existe=False
        else:
            nodo=self.head
            while nodo:
                if dato==nodo.dato:
                    existe=True
                    break
                nodo=nodo.next
        return existe
        
    def devolverNodo(self,dato):
        nodo=self.head
        while nodo:
            if nodo.dato==dato:
                return nodo
            nodo=nodo.next

    def mostrar(self):
        nodo=self.head
        while nodo:
            print(str(nodo.dato)+"->")
            nodo=nodo.next
                
