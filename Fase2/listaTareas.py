import os
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
        self.contador=0
        self.datos={}
        self.reporte=""

    def insertar(self,carnet,nombre,descripcion,materia,fecha,hora,estado):
        nuevo=Nodo(carnet,nombre,descripcion,materia,fecha,hora,estado)
        self.contador+=1
        if self.head==None:
            self.head=nuevo
            self.body=nuevo
            nuevo.index=0
        else:
            self.body.next=nuevo
            nuevo.previous=self.body
            self.body=nuevo
            nuevo.index+=1

    def modificarT(self,nombre,descripcion,materia,fecha,hora,estado,posicion):
        nodo=self.head
        if self.head!=None:
            while(nodo):
                if posicion==nodo.index:
                    nodo.nombre=nombre
                    nodo.descripcion=descripcion
                    nodo.materia=materia
                    nodo.fecha=fecha
                    nodo.hora=hora
                    nodo.estado=estado
                    return
                nodo=nodo.next

    def eliminar(self,posicion):
        nodo=self.head.next
        if posicion==0:
                temp=self.head.next
                self.head.next.previous=None
                self.head.next=None
                self.head=temp
        elif self.body.index==posicion:
            temp=self.body.previous
            temp.next=None
            self.body.previous=None
            self.body=temp
        else:
            while(nodo):
                if nodo.index==posicion:
                    nodo.next.previous=nodo.previous
                    nodo.previous.next=nodo.next
                    nodo.previous=None
                    nodo.next=None
                    return
                nodo=nodo.next

    def mostrarDatos(self,posicion):
        nodo=self.head
        self.datos={}
        if self.head!=None:
            while(nodo):
                if posicion==nodo.index:
                    self.datos["Posición"]=nodo.index
                    self.datos["Carnet"]=nodo.carnet
                    self.datos["Nombre"]=nodo.nombre
                    self.datos["Descripcion"]=nodo.descripcion
                    self.datos["Materia"]=nodo.materia
                    self.datos["Fecha"]=nodo.fecha
                    self.datos["Hora"]=nodo.hora
                    self.datos["Estado"]=nodo.estado
                    return self.datos
                nodo=nodo.next

    def tamaño(self):
        return self.contador

    def graficarDatos(self):
        nodo=self.head
        cont=0
        while nodo:
            if nodo.next!=None:
                self.reporte+=str(cont)+"->"+str(cont+1)+"\n"
            self.reporte+=str(cont)+"[label=\"Carnet: "+nodo.carnet+"\nNombre:"+nodo.nombre+"\nDescripcion:"+nodo.descripcion+"\nMateria:"+nodo.materia+"\nFecha:"+nodo.fecha+"\nHora:"+nodo.hora+"\nEstado:"+nodo.estado+"\"]\n"
            cont+=1
            nodo=nodo.next

        reporte="digraph G{ rankdir=LR node[shape=square] edge[dir=both] "+self.reporte+"}"
        documento=open("C:/Users/osmar/Desktop/Reportes_F2/ListaTareas.dot","w",encoding="utf-8")
        documento.write(reporte)
        documento.close()
        os.system("dot -Tpng C:/Users/osmar/Desktop/Reportes_F2/ListaTareas.dot -o C:/Users/osmar/Desktop/Reportes_F2/ListaTareas.png")


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