from encabezadoMatriz import ListaDatos
from listaTareas import ListaTareas
import os
class Nodo:
    def __init__(self,dia,hora):
        self.dia=dia
        self.hora=hora
        self.datos=ListaTareas()
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
        self.reporte=""

    def insertar(self,dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado):
        cabecera=self.eColumna.head
        while cabecera!=None:
            d=cabecera.puntero
            while d!=None:
                if cabecera.dato==dia and d.hora==hora:
                    d.datos.insertar(carnet,nombre,descripcion,materia,fecha,horaT,estado)
                    return
                d=d.down
            cabecera=cabecera.next
        if cabecera==None or d==None:
            nuevo=Nodo(dia,hora)
            nuevo.datos.insertar(carnet,nombre,descripcion,materia,fecha,horaT,estado)
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
                        if nuevo.hora<temporal.hora:
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
                        if nuevo.dia<temporal.dia:
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
    

    def modificarT(self,nombre,descripcion,materia,fecha,hora,estado,posicion,dia,horaT):
        cabecera=self.eColumna.head
        while cabecera!=None:
            day=cabecera.puntero
            while day!=None:
                if day.hora==horaT and cabecera.dato==dia:
                    day.datos.modificarT(nombre,descripcion,materia,fecha,hora,estado,posicion)
                    return
                day=day.down
            cabecera=cabecera.next

    def eliminarT(self,posicion,dia,horaT):
        cabecera=self.eColumna.head
        while cabecera!=None:
            day=cabecera.puntero
            while day!=None:
                if day.hora==horaT and cabecera.dato==dia:
                    day.datos.eliminar(posicion)
                    return
                day=day.down
            cabecera=cabecera.next

    def verTarea(self,posicion,dia,horaT):
        cabecera=self.eColumna.head
        while cabecera!=None:
            day=cabecera.puntero
            while day!=None:
                if day.hora==horaT and cabecera.dato==dia:
                    mensaje=day.datos.mostrarDatos(posicion)
                    return mensaje
                day=day.down
            cabecera=cabecera.next

    def graficaLT(self,dia,hora):
        cabecera=self.eColumna.head
        while cabecera!=None:
            day=cabecera.puntero
            while day!=None:
                if day.hora==hora and cabecera.dato==dia:
                    day.datos.graficarDatos()
                    return 
                day=day.down
            cabecera=cabecera.next

    def graficarMatriz(self):
        self.mostrarDia()
        self.reporte=""
        self.reporte+="Mat[label=\"Matriz\" group=1]\n"
        self.reporte+=self.eFila.graficarEncabezado("hora")
        self.reporte+=self.eColumna.graficarEncabezado("dia")
        dia=self.eColumna.head
        self.reporte+="Mat->"+"D"+dia.dato+"\n"
        self.reporte+="Mat->"+"H"+self.eFila.head.dato+"\n"
        while dia!=None:
            repo=""
            hora=dia.puntero
            while hora!=None:
                self.reporte+=dia.dato+hora.hora+"[label=\"Tareas\" group="+dia.dato+"]\n"
                if hora.hora==dia.puntero.hora:
                    self.reporte+="D"+dia.dato+"->"+dia.dato+hora.hora+"\n"
                    repo+=dia.dato+hora.hora+";H"+hora.hora+";"
                
                if hora.down!=None:
                    self.reporte+=dia.dato+hora.hora+"->"+dia.dato+hora.down.hora+"\n"
                    self.reporte+=dia.dato+hora.down.hora+"->"+dia.dato+hora.hora+"\n"
                    self.reporte+="{rank=same;"+dia.dato+hora.hora+";H"+hora.hora+";}"
                else:
                    self.reporte+="{rank=same;"+dia.dato+hora.hora+";H"+hora.hora+";}"
                hora=hora.down
            self.reporte+="{rank=same;"+repo+"}\n"
            dia=dia.next

        hora=self.eFila.head
        while hora!=None:
            dia=hora.puntero
            while dia!=None:                                                     
                if dia.dia==hora.puntero.dia:
                    self.reporte+="H"+hora.dato+"->"+dia.dia+hora.dato+"\n"
                    #repo+=dia.dato+hora.hora+";H"+hora.hora+";"
                
                if dia.next!=None:
                    self.reporte+=dia.dia+hora.dato+"->"+dia.next.dia+hora.dato+"\n"
                    self.reporte+=dia.next.dia+hora.dato+"->"+dia.dia+hora.dato+"\n"
                dia=dia.next
            hora=hora.next


        texto="digraph G{\n"+self.reporte+" }"
        documento=open("MatrizTareas.dot","w",encoding="utf-8")
        documento.write(texto)
        documento.close()
        os.system("dot -Tpng MatrizTareas.dot -o MatrizTareas.png")


    def mostrarDia(self):
        cabecera=self.eColumna.head
        while cabecera!=None:
            print("Dia "+str(cabecera.dato))
            dia=cabecera.puntero
            while dia!=None:
                print("Hora: "+str(dia.hora))
                #dia.datos.mostrar()
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