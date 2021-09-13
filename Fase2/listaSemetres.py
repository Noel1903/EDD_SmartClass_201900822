class Nodo:
    def __init__(self,semestre):
        self.semestre=semestre
        self.cursos=None
        self.next=None

class ListaSemestres:
    def __init__(self):
        self.head=None
        self.body=None
        self.cont=0

    def insertar(self,semestre):
        self.cont+=1
        nuevo=Nodo(semestre)
        if self.head==None:
            self.head=nuevo
            self.body=nuevo
        else:
            if self.cont<=2:
                if nuevo.semestre!=self.head.semestre:
                    self.body.next=nuevo
                    self.body=nuevo
                else:
                    print( "No se puede insertar semestre repetido")
            else:
                print( "Solo se pueden contener 2 semestres")
    