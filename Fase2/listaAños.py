from listaMeses import ListaMeses
class NodoA:
    def __init__(self,año):
        self.año=año
        self.semestre=None
        self.meses=ListaMeses()
        self.next=None

class ListaAños:
    def __init__(self) :
        self.head=None
        self.body=None

    def insertar(self,año,mes,dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado):
        nuevo=NodoA(año)
        if self.head==None:
            self.head=nuevo
            self.body=nuevo
            nuevo.meses.insertar(mes,dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado)
        else:
            nodo=self.head
            while nodo!=None:
                if nodo.año==año:
                    nodo.meses.insertar(mes,dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado)
                    return
                nodo=nodo.next
            if nodo==None:
                self.body.next=nuevo
                self.body=nuevo
                nuevo.meses.insertar(mes,dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado)

    def mostrar(self):
        nodo=self.head
        if nodo==None:
            print( "Lista años esta vacia")
        else:
            while(nodo!=None):
                print("Año: "+str(nodo.año))
                nodo.meses.mostrar()
                nodo=nodo.next
