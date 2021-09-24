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

    def modificarT(self,nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT):
        nodo=self.head

        while(nodo):
            if nodo.año==año:
                nodo.meses.modificarT(nombre,descripcion,materia,fecha,hora,estado,posicion,mes,dia,horaT)
                return
            nodo=nodo.next
        if nodo==None:
            return "No existe el año"

    def eliminarT(self,posicion,año,mes,dia,horaT):
        nodo=self.head
        while(nodo):
            if nodo.año==año:
                nodo.meses.eliminarT(posicion,mes,dia,horaT)
                return
            nodo=nodo.next
        if nodo==None:
            return "No existe el año"

    def verTarea(self,posicion,año,mes,dia,horaT):
        nodo=self.head
        while(nodo):
            if nodo.año==año:
                mensaje=nodo.meses.verTarea(posicion,mes,dia,horaT)
                return mensaje
            nodo=nodo.next
        if nodo==None:
            return "No existe el año"

    def graficaLT(self,año,mes,dia,hora):
        nodo=self.head
        while(nodo):
            if nodo.año==año:
                nodo.meses.graficaLT(mes,dia,hora)
                return
            nodo=nodo.next
        if nodo==None:
            print( "No existe el año")

    def graficaM(self,año,mes):
        nodo=self.head
        while(nodo):
            if nodo.año==año:
                nodo.meses.graficaM(mes)
                return
            nodo=nodo.next
        if nodo==None:
            print( "No existe el año")

    def mostrar(self):
        nodo=self.head
        if nodo==None:
            print( "Lista años esta vacia")
        else:
            while(nodo!=None):
                print("Año: "+str(nodo.año))
                nodo.meses.mostrar()
                nodo=nodo.next
