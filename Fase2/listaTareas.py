class Nodo:
    def __init__(self,carnet,nombre,descripcion,materia,fecha,hora,estado):
        self.carnet=carnet
        self.nombre=nombre
        self.descripcion=descripcion
        self.materia=materia
        self.fecha=fecha
        self.hora=hora
        self.estado=estado
        self.index=0
        self.next=None
        self.previous=None

class ListaTareas:
    def __init__(self):
        self.head=None
        self.body=None

    def insertar(self,carnet,nombre,descripcion,materia,fecha,hora,estado):
        nuevo=Nodo(carnet,nombre,descripcion,materia,fecha,hora,estado)
        if self.head==None:
            self.head=nuevo
            self.body=nuevo
        else:
            self.body.next=nuevo
            nuevo.previous=self.body
            self.body=nuevo
            nuevo.index+=1

    def mostrar(self):
        nodo=self.head
        if self.head!=None:
            while(nodo):
                print(nodo.index)
                print(nodo.carnet)
                print(nodo.nombre)
                print(nodo.descripcion)
                print(nodo.materia)
                print(nodo.hora)
                print(nodo.estado)
                nodo=nodo.next
        
    def mostrarI(self):
        nodo=self.body
        if self.head!=None:
            while(nodo):
                print(nodo.datos)
                nodo=nodo.previous