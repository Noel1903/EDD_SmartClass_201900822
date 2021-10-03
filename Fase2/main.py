"""from listaAños import ListaAños
from listaSemetres import ListaSemestres
from listaMeses import ListaMeses
from encabezadoMatriz import ListaDatos
from listaMatriz import Matriz
from ArbolAVL import Arbol
mes=ListaMeses()
anios=ListaAños()
semestres=ListaSemestres()
encabezados=ListaDatos()
matriz=Matriz()
arbol=Arbol()
anios.mostrar()
anios.insertar(2021)
anios.insertar(2020)
anios.insertar(2018)
anios.insertar(2015)
anios.mostrar()

semestres.insertar(2)
semestres.insertar(1)
semestres.insertar(1)

mes.insertar(2)
mes.insertar(10)
mes.insertar(8)
mes.mostrar()
mes.mostrarI()
print("----------------------------")
#print(encabezados.insertar(2))
#encabezados.insertar(8)
#encabezados.insertar(5)
#print(encabezados.insertar(3))
#encabezados.insertar(1)
#encabezados.mostrar()
matriz.insertar(1,16,5)
matriz.insertar(1,12,5)
matriz.insertar(3,4,7)
matriz.insertar(4,1,9)
matriz.insertar(2,8,11)
matriz.insertar(5,12,4)
matriz.mostrarDia()
print("---------")
matriz.mostrarHora()

arbol.insertar(5,2020)
arbol.insertar(2,2019)
arbol.insertar(1,2021)
arbol.mostrar()"""
"""dicc={}
dicc['Edad']=21
dicc['Nombre']="Noel"
print(dicc)"""
"""from ArbolBCursos import ArbolB
btree=ArbolB()

btree.insertar(101,"EDD",5,"Hola","Obligatorio")
btree.insertar(301,"IPC",4,"Hola","Obligatorio")
btree.insertar(400,"Lenguajes",8,"Hola","Obligatorio")
btree.insertar(205,"Matematica",6,"Hola","Obligatorio")
btree.insertar(95,"Orga",1,"Hola","Obligatorio")
btree.mostrar()"""
"""for i in range(5):
    print (i)"""

"""def compareTo(a,b):
        if a==b:
            return 0
        elif b<a:
            return -1
        else:
            return 1

print(compareTo("b","b"))"""
from ArbolBCursos import ArbolB

nuevo=ArbolB()

nuevo.insertarDatos(301,"EDD",10,"201,406,303","Si")
nuevo.insertarDatos(201,"Apli1",10,"201,406,303","Si")
nuevo.insertarDatos(100,"EDD",10,"201,406,303","Si")
nuevo.insertarDatos(80,"EDD",10,"201,406,303","Si")
nuevo.insertarDatos(550,"EDD",10,"201,406,303","Si")
nuevo.insertarDatos(1023,"EDD",10,"201,406,303","Si")
nuevo.insertarDatos(100,"EDD",10,"201,406,303","Si")
nuevo.insertarDatos(98,"EDD",10,"201,406,303","Si")
nuevo.insertarDatos(25,"EDD",10,"201,406,303","Si")
nuevo.Preorder()