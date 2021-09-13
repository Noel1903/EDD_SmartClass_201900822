class NodoA:
    def __init__(self,año):
        self.año=año
        self.semestre=None
        self.meses=None
        self.next=None

class ListaAños:
    def __init__(self) :
        self.head=None
        self.body=None

    def insertar(self,año):
        nuevo=NodoA(año)
        if self.head==None:
            self.head=nuevo
            self.body=nuevo
        else:
            self.body.next=nuevo
            self.body=nuevo

    def mostrar(self):
        nodo=self.head
        if nodo==None:
            print( "Lista años esta vacia")
        else:
            while(nodo!=None):
                print(nodo.año)
                nodo=nodo.next
