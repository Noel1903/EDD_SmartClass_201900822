import os
class NodoD:
    def __init__(self,codigo,nombre,creditos,prerrequisitos,obligatorio):
        self.codigo=codigo
        self.nombre=nombre
        self.creditos=creditos
        self.prerrequisitos=prerrequisitos
        self.obligatorio=obligatorio
        self.next=None
        self.previous=None

class NodoP:
    def __init__(self,puntero):
        self.puntero=puntero
        self.next=None
        self.previous=0

class ListaD:
    def __init__(self):
        self.head=None
        self.body=None
        self.contador=0

    def vacio(self):
        if self.head==None:
            return True
        else:
            return False
    
    def insertarN(self,codigo,nombre,creditos,prerrequisitos,obligatorio):
        nuevo=NodoD(codigo,nombre,creditos,prerrequisitos,obligatorio)
        if self.contador<4:
            if self.vacio():
                self.head=nuevo
                self.body=nuevo
            else:
                self.body.next=nuevo
                nuevo.previous=self.body
                self.body=nuevo
            self.contador+=1

    def insertarDato(self,codigo,posicion):
        nodo=self.head
        while posicion!=0:
            posicion-=1
            nodo=nodo.next
        nodo.codigo=codigo

    def devolverDato(self,posicion):
        nodo=self.head
        while posicion!=0:
            posicion-=1
            nodo=nodo.next
        return nodo

class ListaP:
    def __init__(self):
        self.head=None
        self.body=None
        self.contador=0
    
    def vacio(self):
        if self.head==None:
            return True
        else:
            return False
    
    def insertarP(self,puntero):
        nuevo=NodoP(puntero)
        if self.contador<5:
            if self.vacio():
                self.head=nuevo
                self.body=nuevo
            else:
                self.body.next=nuevo
                nuevo.previous=self.body
                self.body=nuevo
            self.contador+=1

    def insertarPuntero(self,pagina,posicion):
        nodo=self.head
        while posicion!=0:
            posicion-=1
            nodo=nodo.next
        nodo.puntero=pagina

    def devolverPuntero(self,posicion):
        nodo=self.head
        while posicion!=0:
            posicion-=1
            nodo=nodo.next
        return nodo

class Pagina:
    def __init__(self):
        self.contador=0
        self.maximo=5
        self.punteros=ListaP()
        self.datos=ListaD()
        for i in range(5):
            if i!=4:
                self.datos.insertarN(None,"",None,"",None)
            self.punteros.insertarP(None)
        
    def paginaLlena(self):
        if self.contador==self.maximo-1:
            return True
        else:
            return False
    
    def getContador(self):
        return self.contador
    
    def setContador(self,contador):
        self.contador=contador

    def paginaCasiLlena(self):
        if self.contador==self.maximo/2:
            return True
        else:
            return False

    def setCodigo(self,posicion,codigo):
        self.datos.insertarDato(codigo,posicion)
    
    def setNombre(self,posicion,nombre):
        self.datos.devolverDato(posicion).nombre=nombre
    
    def setCreditos(self,posicion,creditos):
        self.datos.devolverDato(posicion).creditos=creditos
    
    def setPrerrequisitos(self,posicion,prerrequisitos):
        self.datos.devolverDato(posicion).prerrequisitos=prerrequisitos
    
    def setObligatorio(self,posicion,obligario):
        self.datos.devolverDato(posicion).obligatorio=obligario

    def getCodigo(self,posicion):
        return self.datos.devolverDato(posicion).codigo
    
    def getNombre(self,posicion):
        return self.datos.devolverDato(posicion).nombre

    def getCreditos(self,posicion):
        return self.datos.devolverDato(posicion).creditos

    def getPrerrequisitos(self,posicion):
        return self.datos.devolverDato(posicion).prerrequisitos

    def getObligatorio(self,posicion):
        return self.datos.devolverDato(posicion).obligatorio
    
    def setPuntero(self,posicion,puntero):
        self.punteros.insertarPuntero(puntero,posicion)
    
    def getPuntero(self,posicion):
        return self.punteros.devolverPuntero(posicion).puntero

    def getCodigo(self,posicion):
        return self.datos.devolverDato(posicion).codigo

class ArbolB:
    def __init__(self):
        self.raiz=None
        self.aux1=False
        self.aux2=None
        self.subeA=False
        self.estado=False
        self.comparador=False
        self.grafica=""
        self.nodos=0
        self.Codigo=""
        self.Nombre=""
        self.Creditos=0
        self.Prerrequisitos=""
        self.Obligatorio=""

    def Vacio(self,raiz):
        if raiz==None or raiz.contador==0:
            return True
        else:
            return False

    def insertarDatos(self,codigo,nombre,creditos,prerrequisitos,obligatorio):
        self.insertarDatos01(self.raiz,codigo,nombre,creditos,prerrequisitos,obligatorio)

    def insertarDatos01(self,raiz,codigo,nombre,creditos,prerrequisitos,obligatorio):
        self.Empujar(raiz,codigo,nombre,creditos,prerrequisitos,obligatorio)
        if self.subeA:
            self.raiz=Pagina()
            self.raiz.setContador(1)
            self.raiz.setCodigo(0,self.Codigo)
            self.raiz.setNombre(0,self.Nombre)
            self.raiz.setCreditos(0,self.Creditos)
            self.raiz.setPrerrequisitos(0,self.Prerrequisitos)
            self.raiz.setObligatorio(0,self.Obligatorio)
            self.raiz.setPuntero(0,raiz)
            self.raiz.setPuntero(1,self.aux2)

    def Empujar(self,raiz,codigo,nombre,creditos,prerrequisitos,obligatorio):
        posicion=0
        self.estado=False
        if self.Vacio(raiz) and self.comparador==False:
            self.subeA=True
            self.Codigo=codigo
            self.Nombre=nombre
            self.Creditos=creditos
            self.Prerrequisitos=prerrequisitos
            self.Obligatorio=obligatorio
            self.aux2=None
        else:
            posicion=self.buscarN(codigo,raiz)
            if self.comparador==False:
                if self.estado:
                    self.subeA=False
                else:
                    self.Empujar(raiz.getPuntero(posicion),codigo,nombre,creditos,prerrequisitos,obligatorio)
                    if self.subeA:
                        if raiz.getContador()<4:
                            self.subeA=False
                            self.meterHoja(raiz,posicion,self.Codigo,self.Nombre,self.Creditos,self.Prerrequisitos,self.Obligatorio)
                        else:
                            self.subeA=True
                            self.dividir(raiz,posicion,self.Codigo,self.Nombre,self.Creditos,self.Prerrequisitos,self.Obligatorio)
            else:
                self.comparador=False

    def buscarN(self,codigo,raiz):
        contadorA=0
        if self.compareTo(raiz.getCodigo(0),codigo)<0:
            self.estado=False
            contadorA=0
        else:
            while contadorA!=raiz.getContador():
                if codigo==raiz.getCodigo(contadorA):
                    self.comparador=True
                contadorA+=1
            contadorA=raiz.getContador()

            while self.compareTo(raiz.getCodigo(contadorA-1),codigo)<0 and contadorA>1:
                contadorA-=1
                if codigo==raiz.getCodigo(contadorA-1):
                    self.estado=True
                else:
                    self.estado=False
        return contadorA            

    def compareTo(self,a,b):
        if a==b:
            return 0
        elif b<a:
            return -1
        else:
            return 1
    
    def meterHoja(self,raiz,posicion,codigo,nombre,creditos,prerrequisitos,obligatorio):
        contA=raiz.getContador()
        while contA!=posicion:
            if contA!=0:
                raiz.setCodigo(contA,raiz.getCodigo(contA-1))
                raiz.setNombre(contA,raiz.getNombre(contA-1))
                raiz.setCreditos(contA,raiz.getCreditos(contA-1))
                raiz.setPrerrequisitos(contA,raiz.getPrerrequisitos(contA-1))
                raiz.setObligatorio(contA,raiz.getObligatorio(contA-1))
                raiz.setPuntero(contA+1,raiz.getPuntero(contA))
            contA-=1

        raiz.setCodigo(posicion,codigo)
        raiz.setNombre(posicion,nombre)
        raiz.setCreditos(posicion,creditos)
        raiz.setPrerrequisitos(posicion,prerrequisitos)
        raiz.setObligatorio(posicion,obligatorio)
        raiz.setPuntero(posicion+1,self.aux2)
        raiz.setContador(raiz.getContador()+1)

    def dividir(self,raiz,posicion,codigo,nombre,creditos,prerrequisitos,obligatorio):
        posicion2=0
        posicionM=0
        if posicion<=2:
            posicionM=2
        else:
            posicionM=3
        paginaD=Pagina()
        posicion2=posicionM+1
        while posicion2!=5:
            if (posicion2-posicionM)!=0:
                paginaD.setCodigo((posicion2-posicionM)-1,raiz.getCodigo(posicion2-1))
                paginaD.setNombre((posicion2-posicionM)-1,raiz.getNombre(posicion2-1))
                paginaD.setCreditos((posicion2-posicionM)-1,raiz.getCreditos(posicion2-1))
                paginaD.setPrerrequisitos((posicion2-posicionM)-1,raiz.getPrerrequisitos(posicion2-1))
                paginaD.setObligatorio((posicion2-posicionM)-1,raiz.getObligatorio(posicion2-1))
                paginaD.setPuntero(posicion2-posicionM,raiz.getPuntero(posicion2))
            posicion2+=1

        paginaD.setContador(4-posicionM)
        raiz.setContador(posicionM)
        if posicion<=2:
            self.aux1=True
            self.meterHoja(raiz,posicion,codigo,nombre,creditos,prerrequisitos,obligatorio)
        else:
            self.aux1=True
            self.meterHoja(paginaD,(posicion-posicionM),codigo,nombre,creditos,prerrequisitos,obligatorio)
        self.Codigo=raiz.getCodigo(raiz.getContador()-1)
        self.Nombre=raiz.getNombre(raiz.getContador()-1)
        self.Creditos=raiz.getCreditos(raiz.getContador()-1)
        self.Prerrequisitos=raiz.getPrerrequisitos(raiz.getContador()-1)
        self.Obligatorio=raiz.getObligatorio(raiz.getContador()-1)
        paginaD.setPuntero(0,raiz.getPuntero(raiz.getContador()))
        raiz.setContador(raiz.getContador()-1)
        self.aux2=paginaD
        if self.aux1:
            raiz.setCodigo(3,"")
            raiz.setNombre(3,"")
            raiz.setCreditos(3,"")
            raiz.setPrerrequisitos(3,"")
            raiz.setObligatorio(3,"")
            raiz.setPuntero(4,None)

            raiz.setCodigo(2,"")
            raiz.setNombre(2,"")
            raiz.setCreditos(2,"")
            raiz.setPrerrequisitos(2,"")
            raiz.setObligatorio(2,"")
            raiz.setPuntero(3,None)

    def Preorder(self):
        self.Preorder01(self.raiz)

    def Preorder01(self,raiz):
        if raiz!=None:
            for i in range(raiz.getContador()):
                if raiz.getCodigo(i)!=None:
                    print(raiz.getCodigo(i),end="_")
            print("")
            self.Preorder01(raiz.getPuntero(0))
            self.Preorder01(raiz.getPuntero(1))
            self.Preorder01(raiz.getPuntero(2))
            self.Preorder01(raiz.getPuntero(3))
            self.Preorder01(raiz.getPuntero(4))

    
    def graficar(self):
        self.grafica=""
        self.graficar01(self.raiz)
        self.graficar02(self.raiz)

        grafica="digraph ArbolBCursos{\n rankdir=TB\n node [shape=record]\n"+self.grafica+"\n}"
        documento=open("C:/Users/osmar/Desktop/Reportes_F2/CursosEstudiante.dot","w",encoding="utf-8")
        documento.write(grafica)
        documento.close()
        os.system("dot -Tpng C:/Users/osmar/Desktop/Reportes_F2/CursosEstudiante.dot -o C:/Users/osmar/Desktop/Reportes_F2/CursosEstudiante.png")


    def graficar01(self,raiz):
        contador=0
        if raiz!=None:
            self.nodos=0
            for i in range(raiz.getContador()):
                if raiz.getCodigo(i)!="":
                    self.nodos+=1
                    if i!=0:
                        self.grafica+="|"
                    if self.nodos==1:
                        self.grafica+="\nNodo"+raiz.getCodigo(i)+"[label=\"<f0> |"
                    if i==0:
                        self.grafica+="<f"+str(i+1)+"->"+raiz.getCodigo(i)+"\\n"+raiz.getNombre(i)+"|<f"+str(i+2)+"> "
                        contador=3
                    else:
                        self.grafica+="<f"+str(contador)+">"+raiz.getCodigo(i)+"\\n"+raiz.getNombre(i)+"|<f"+str(contador+1)+"> "
                        contador+=2
                    
                    if i==raiz.getContador()-1:
                        contador=0
                        self.grafica+="\",group=0];\n"

            self.graficar01(raiz.getPuntero(0))
            self.graficar01(raiz.getPuntero(1))
            self.graficar01(raiz.getPuntero(2))
            self.graficar01(raiz.getPuntero(3))
            self.graficar01(raiz.getPuntero(4))


    def graficar02(self,raiz):
        if raiz!=None:
            if raiz.getCodigo(0)!=None:
                if raiz.getCodigo(0)!="":
                    if raiz.getPuntero(0)!=None and raiz.getPuntero(0).getCodigo(0)!=None:
                        self.grafica+="\nNodo"+raiz.getCodigo(0)+":f0->"+"Nodo"+raiz.getPuntero(0).getCodigo(0)
                    if raiz.getPuntero(1)!=None and raiz.getPuntero(1).getCodigo(0)!=None:
                        self.grafica+="\nNodo"+raiz.getCodigo(0)+":f2->"+"Nodo"+raiz.getPuntero(1).getCodigo(0)
                    if raiz.getPuntero(2)!=None and raiz.getPuntero(2).getCodigo(0)!=None:
                        self.grafica+="\nNodo"+raiz.getCodigo(0)+":f4->"+"Nodo"+raiz.getPuntero(2).getCodigo(0)
                    if raiz.getPuntero(3)!=None and raiz.getPuntero(3).getCodigo(0)!=None:
                        self.grafica+="\nNodo"+raiz.getCodigo(0)+":f6->"+"Nodo"+raiz.getPuntero(3).getCodigo(0)
                    if raiz.getPuntero(4)!=None and raiz.getPuntero(4).getCodigo(0)!=None:
                        self.grafica+="\nNodo"+raiz.getCodigo(0)+":f8->"+"Nodo"+raiz.getPuntero(4).getCodigo(0)

            self.graficar02(raiz.getPuntero(0))
            self.graficar02(raiz.getPuntero(1))
            self.graficar02(raiz.getPuntero(2))
            self.graficar02(raiz.getPuntero(3))
            self.graficar02(raiz.getPuntero(4))
