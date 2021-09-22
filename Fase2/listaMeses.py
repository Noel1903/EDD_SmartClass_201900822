from typing import List
from listaMatriz import Matriz
class Nodo:
    def __init__(self,mes):
        self.mes=mes
        self.tareas=Matriz()
        self.next=None
        self.previous=None

class ListaMeses:
    def __init__(self):
        self.head=None
        self.body=None

    def insertar(self,mes,dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado):
        nuevo=Nodo(mes)
        if self.head==None:
            self.head=nuevo
            self.body=nuevo
            nuevo.tareas.insertar(dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado)
        else:
            nodo=self.head
            while nodo!=None:
                if mes==nodo.mes:
                    nodo.tareas.insertar(dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado)
                    return
                nodo=nodo.next
            if nodo==None:
                self.body.next=nuevo
                nuevo.previous=self.body
                self.body=nuevo
                nuevo.tareas.insertar(dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado)

    def mostrar(self):
        nodo=self.head
        if self.head!=None:
            while(nodo):
                print("Mes:"+str(nodo.mes))
                nodo.tareas.mostrarDia()
                nodo=nodo.next
        
    def mostrarI(self):
        nodo=self.body
        if self.head!=None:
            while(nodo):
                print(nodo.mes)
                nodo=nodo.previous