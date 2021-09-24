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
        self.reporte=""
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

    def graficarEncabezado(self,tipo):
        nodo=self.head
        self.reporte=""
        rank=""
        if tipo=="hora":
            while nodo:
                self.reporte+="H"+nodo.dato+"[label=\"Hora:"+nodo.dato+"\" group=1]\n"
                nodo=nodo.next

            nodo=self.head
            while nodo.next!=None:
                self.reporte+="H"+nodo.dato+"->H"+nodo.next.dato+"\n"
                self.reporte+="H"+nodo.next.dato+"->H"+nodo.dato+"\n"
                nodo=nodo.next
            return self.reporte
        else:
            cont=2
            while nodo:
                self.reporte+="D"+nodo.dato+"[label=\"Dia:"+nodo.dato+"\" group="+nodo.dato+"]\n"
                cont+=1
                rank+="D"+nodo.dato+"; "
                nodo=nodo.next
            nodo=self.head
            while nodo.next!=None:
                self.reporte+="D"+nodo.dato+"->D"+nodo.next.dato+"\n"
                self.reporte+="D"+nodo.next.dato+"->D"+nodo.dato+"\n"
                nodo=nodo.next
            return self.reporte+"{rank = same;Mat;"+rank+"}\n"

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
                
