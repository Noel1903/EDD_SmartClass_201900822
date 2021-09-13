from encabezadoMatriz import ListaDatos
class Nodo:
    def __init__(self,dia,hora,dato):
        self.dia=dia
        self.hora=hora
        self.dato=dato
        self.next=None
        self.previous=None
        self.up=None
        self.down=None

class Matriz:
    def __init__(self):
        self.eFila=ListaDatos()
        self.eColumna=ListaDatos()
        self.dato=None
        self.primero=None

    def insertar(self,dia,hora,dato):
        nuevo=Nodo(dia,hora,dato)
        if self.eColumna.existe(dia)!=True:
            self.eColumna.insertar(dia)
        datoC=self.eColumna.devolverNodo(dia)
        if datoC.dato==dia:
            if datoC.puntero==None:
                datoC.puntero=nuevo
                self.primero=nuevo
                self.dato=nuevo
            elif nuevo.hora<datoC.puntero.hora:
                datoC.up=nuevo
                nuevo.down=datoC.puntero
                datoC.puntero=nuevo
                self.primero=nuevo
                self.dato=datoC
            else:
                temporal=datoC.puntero
                while temporal.down!=None:
                    if nuevo.hora<temporal.dato:
                        nuevo.down=temporal.down
                        temporal.down.up=nuevo
                        nuevo.up=temporal 
                        temporal.down=nuevo                      
                        self.dato=nuevo
                        break                           
                    temporal=temporal.down

                if temporal.down==None:                      
                        temporal.down=nuevo
                        nuevo.up=temporal
                        self.dato=nuevo

        if self.eFila.existe(hora)!=True:
            self.eFila.insertar(hora)
        datoF=self.eFila.devolverNodo(hora)

        if datoF.dato==hora:
            if datoF.puntero==None:
                datoF.puntero=nuevo
                self.primero=nuevo
                self.dato=nuevo
            elif nuevo.dia<datoF.puntero.dia:
                datoF.previous=nuevo
                nuevo.next=datoF.puntero
                datoF.puntero=nuevo
                self.primero=nuevo
                self.dato=datoF
            else:
                temporal=datoF.puntero
                while temporal.next!=None:
                    if nuevo.dia<temporal.dato:
                        nuevo.next=temporal.next
                        temporal.next.previous=nuevo
                        nuevo.previous=temporal 
                        temporal.next=nuevo                      
                        self.dato=nuevo
                        break                           
                    temporal=temporal.next

                if temporal.next==None:                      
                        temporal.next=nuevo
                        nuevo.previous=temporal
                        self.dato=nuevo
    
    def mostrarDia(self):
        cabecera=self.eColumna.head
        while cabecera!=None:
            print("Dia "+str(cabecera.dato))
            dia=cabecera.puntero
            while dia!=None:
                print("Hora: "+str(dia.hora))
                dia=dia.down
            cabecera=cabecera.next

    def mostrarHora(self):
        cabecera=self.eFila.head
        while cabecera!=None:
            print("Hora "+str(cabecera.dato))
            dia=cabecera.puntero
            while dia!=None:
                print("Dia: "+str(dia.dia))
                dia=dia.next
            cabecera=cabecera.next