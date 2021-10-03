from CursosEstudiante import ArbolB
class Nodo:
    def __init__(self,semestre):
        self.semestre=semestre
        self.cursos=ArbolB()
        self.next=None

class ListaSemestres:
    def __init__(self):
        self.head=None
        self.body=None
        
        self.cont=0

    def insertar(self,semestre,datos):
        self.cont+=1
        nuevo=Nodo(semestre)
        if self.head==None:
            self.head=nuevo
            self.body=nuevo
            for i in datos:
                nuevo.cursos.insertarDatos(i["Codigo"],i["Nombre"],i["Creditos"],i["Prerequisitos"],i["Obligatorio"])
        else:
            if self.cont<=2:
                if nuevo.semestre!=self.head.semestre:
                    self.body.next=nuevo
                    self.body=nuevo
                    for i in datos:
                        nuevo.cursos.insertarDatos(i["Codigo"],i["Nombre"],i["Creditos"],i["Prerequisitos"],i["Obligatorio"])
                else:
                    print( "No se puede insertar semestre repetido")
            else:
                print( "Solo se pueden contener 2 semestres")
    
    def graficaCursos(self,semestre):
        nodo=self.head
        while nodo:
            if nodo.semestre==semestre:
                nodo.cursos.graficar()
            nodo=nodo.next