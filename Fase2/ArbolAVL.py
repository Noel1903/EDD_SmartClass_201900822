from flask.json import jsonify
from listaAños import ListaAños
import os
class Hoja:
    def __init__(self,carnet,dpi,nombre,carrera,correo,password,creditos,edad):
        self.carnet=carnet
        self.dpi=dpi
        self.nombre=nombre
        self.carrera=carrera
        self.correo=correo
        self.password=password
        self.creditos=creditos
        self.edad=edad
        self.años=ListaAños()
        self.left=None
        self.right=None
        self.height=0
        
        

class Arbol:
    def __init__(self):
        self.root=None
        self.existe=False
        self.reporte=""
        self.contador=0
        self.estudiante={}

    def max(self,n1,n2):
        return max(n1,n2)

    def height(self,root):
        if root!=None:
            return root.height
        return -1

    def insertar(self,carnet,dpi,nombre,carrera,correo,password,creditos,edad):
        self.root=self.insertarHoja(carnet,dpi,nombre,carrera,correo,password,creditos,edad,self.root)
        
    def insertarHoja(self,carnet,dpi,nombre,carrera,correo,password,creditos,edad,root):
        if root==None:
            nuevo=Hoja(carnet,dpi,nombre,carrera,correo,password,creditos,edad)
            #anios=ListaAños()
            #nuevo.años=anios
            #anios.insertar(año)
            return nuevo
        elif carnet>root.carnet:
           root.right=self.insertarHoja(carnet,dpi,nombre,carrera,correo,password,creditos,edad,root.right)
           if self.height(root.right)-self.height(root.left)==2:
                if carnet<root.right.carnet:
                   root=self.Doble_rotD(root)
                else:
                    root=self.rotacionI(root)
        elif carnet<root.carnet:
            root.left=self.insertarHoja(carnet,dpi,nombre,carrera,correo,password,creditos,edad,root.left)
            if self.height(root.left)-self.height(root.right)==2:
                if carnet>root.left.carnet:
                   root=self.Doble_rotI(root)
                else:
                    root=self.rotacionD(root)
        #else:
            #root.años.insertar(año)
        root.height=self.max(self.height(root.left),self.height(root.right))+1

        return root
    
    def modificar(self,carnet,dpi,nombre,carrera,correo,password,creditos,edad):
        if carnet<self.root.carnet:
            self.modificar_n(carnet,dpi,nombre,carrera,correo,password,creditos,edad,self.root.left)
        elif carnet>self.root.carnet:
            self.modificar_n(carnet,dpi,nombre,carrera,correo,password,creditos,edad,self.root.right)
        elif carnet==self.root.carnet:
            self.root.dpi=dpi
            self.root.nombre=nombre
            self.root.carrera=carrera
            self.root.correo=correo
            self.root.password=password
            self.root.creditos=creditos
            self.root.edad=edad
            self.existe=True

        if self.existe:
            self.existe=False
            return "Alumno modificado correctamente"
        else:
            return "No existe el alumno o los datos son incorrectos"
        
    def modificar_n(self,carnet,dpi,nombre,carrera,correo,password,creditos,edad,root):
        
        if root!=None:
            if carnet==root.carnet:
                root.dpi=dpi
                root.nombre=nombre
                root.carrera=carrera
                root.correo=correo
                root.password=password
                root.creditos=creditos
                root.edad=edad
                self.existe=True
            elif carnet<root.carnet:
                self.modificar_n(carnet,dpi,nombre,carrera,correo,password,creditos,edad,root.left)
            elif carnet>root.carnet:
                self.modificar_n(carnet,dpi,nombre,carrera,correo,password,creditos,edad,root.right)

    def mostrarEstudiante(self,carnet):
        self.estudiante={}
        if carnet==self.root.carnet:
            self.estudiante["DPI"]=self.root.dpi
            self.estudiante["Nombre"]=self.root.nombre
            self.estudiante["Carrera"]=self.root.carrera
            self.estudiante["Corrreo"]=self.root.correo
            self.estudiante["Password"]=self.root.password
            self.estudiante["Creditos"]=self.root.creditos
            self.estudiante["Edad"]=self.root.edad
        elif carnet<self.root.carnet:
            self.mostrarEstudiante01(carnet,self.root.left)
        elif carnet>self.root.carnet:
            self.mostrarEstudiante01(carnet,self.root.right)  

        if self.estudiante!=None:
            return self.estudiante
        else:
            return "No existe el carnet"

         

    def mostrarEstudiante01(self,carnet,root):
        if root!=None:
            if carnet==root.carnet:
                self.estudiante["DPI"]=root.dpi
                self.estudiante["Nombre"]=root.nombre
                self.estudiante["Carrera"]=root.carrera
                self.estudiante["Corrreo"]=root.correo
                self.estudiante["Password"]=root.password
                self.estudiante["Creditos"]=root.creditos
                self.estudiante["Edad"]=root.edad
               
            elif carnet<root.carnet:
                self.mostrarEstudiante01(carnet,root.left)
            elif carnet>root.carnet:
                self.mostrarEstudiante01(carnet,root.right)


    def rotacionD(self,root):
        temp=root.left
        root.left=temp.right
        temp.right=root
        root.height=max(self.height(root.left),self.height(root.right))+1
        temp.height=max(self.height(temp.left),self.height(temp.right))+1
        return temp
    
    def rotacionI(self,root):
        temp=root.right
        root.right=temp.left
        temp.left=root
        root.height=max(self.height(root.left),self.height(root.right))+1
        temp.height=max(self.height(temp.left),self.height(temp.right))+1
        return temp

    def Doble_rotD(self,root):
        root.right=self.rotacionD(root.right)
        return self.rotacionI(root)
    
    def Doble_rotI(self,root):
        root.left=self.rotacionI(root.left)
        return self.rotacionD(root)

    def imprimir(self):
        if self.root==None:
            return
        self.imprimir_preorder(self.root)
    
    def imprimir_preorder(self,root):
        print(root.carnet)
        if root.left!=None:
            self.imprimir_preorder(root.left)
        if root.right!=None:
            self.imprimir_preorder(root.right)
        

    def insertarAño(self,carnet,año,mes,dia,hora,nombre,descripcion,materia,fecha,horaT,estado):
        self.insertarA(carnet,año,mes,dia,hora,nombre,descripcion,materia,fecha,horaT,estado,self.root)
    
    def insertarA(self,carnet,año,mes,dia,hora,nombre,descripcion,materia,fecha,horaT,estado,root):
        if carnet==root.carnet:
            root.años.insertar(año,mes,dia,hora,carnet,nombre,descripcion,materia,fecha,horaT,estado)
            #print(str(carnet)+":"+str(año))
        elif carnet<root.carnet:
            self.insertarA(carnet,año,mes,dia,hora,nombre,descripcion,materia,fecha,horaT,estado,root.left)
        if carnet>root.carnet:
            self.insertarA(carnet,año,mes,dia,hora,nombre,descripcion,materia,fecha,horaT,estado,root.right)
    
    def mostrarA(self):
        self.mostrarAños(self.root)

    def mostrarAños(self,root):
        print(root.carnet)
        root.años.mostrar()
        if root.left!=None:
            self.mostrarAños(root.left)
        if root.right!=None:
            self.mostrarAños(root.right)

    def graficarArbol(self):
        contador=0
        cont=0
        self.reporte=""
        if self.root==None:
            return
        self.graficarArbol01(self.root,contador,cont)
        #self.reporte+=str(self.contador)+"[label=\""+self.root.carnet+"\n"+self.root.dpi+"\n"+self.root.nombre+"\n"+self.root.carrera+"\n"+self.root.correo+"\n"+self.root.password+"\n"+self.root.creditos+"\n"+self.root.edad+"\n\"]"
        documento="digraph G{node[shape=\"rectangle\"] "+self.reporte+" }" 
        reporte=open("C:/Users/osmar/Desktop/Reportes_F2/ReporteEstudiantes.dot","w",encoding="utf-8")
        reporte.write(documento)    
        reporte.close()
        os.system("dot -Tpng C:/Users/osmar/Desktop/Reportes_F2/ReporteEstudiantes.dot -o C:/Users/osmar/Desktop/Reportes_F2/ReporteEstudiantes.png")

    def graficarArbol01(self,root,contador,cont):
        if root!= None:
            self.reporte+=str(contador)+"[label=\""+str(root.carnet)+"\n"+root.dpi+"\n"+root.nombre+"\n"+root.carrera+"\n"+root.correo+"\n"+root.password+"\n"+str(root.creditos)+"\n"+str(root.edad)+"\n\"]"
            #self.reporte+=str(contador)+"[label=\""+str(root.carnet)+"\n"+root.dpi+"\n"+root.nombre+"\n"+root.carrera+"\n"+root.correo+"\n"+root.password+"\n"+str(root.creditos)+"\n"+str(root.edad)+"\n\"]"  
            cont=contador
            contador+=1
            self.contador=contador
            if root.left!=None:
                
                
                self.reporte+=str(cont)+"->"+str(contador)+"\n"
                self.graficarArbol01(root.left,contador,cont)
                #self.reporte+=str(self.contador+contador-1)+"->"+str(contador+1)
            if root.right!=None:
                contador=self.contador+1
                self.reporte+=str(cont)+"->"+str(contador)+"\n"
                self.graficarArbol01(root.right,contador,cont)
                self.contador=contador

    def modificarTarea(self,carnet,nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT):
        if carnet<self.root.carnet:
            self.modificar_T(carnet,nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT,self.root.left)
        elif carnet>self.root.carnet:
            self.modificar_T(carnet,nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT,self.root.right)
        elif carnet==self.root.carnet:
            self.root.años.modificarT(nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT)
            self.existe=True

    def modificar_T(self,carnet,nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT,root):
        if root!=None:
            if carnet==root.carnet:
                root.años.modificarT(nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT)
                self.existe=True
            elif carnet<root.carnet:
                self.modificar_T(carnet,nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT,root.left)
            elif carnet>root.carnet:
                self.modificar_T(carnet,nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT,root.right)      
                
    def eliminarT(self,carnet,posicion,año,mes,dia,horaT):
        if carnet<self.root.carnet:
            self.eliminar_T(carnet,posicion,año,mes,dia,horaT,self.root.left)
        elif carnet>self.root.carnet:
            self.eliminar_T(carnet,posicion,año,mes,dia,horaT,self.root.right)
        elif carnet==self.root.carnet:
            self.root.años.eliminarT(carnet,posicion,año,mes,dia,horaT)
            self.existe=True

    def eliminar_T(self,carnet,posicion,año,mes,dia,horaT,root):
        if root!=None:
            if carnet==root.carnet:
                root.años.eliminarT(posicion,año,mes,dia,horaT)
                self.existe=True
            elif carnet<root.carnet:
                self.eliminar_T(carnet,posicion,año,mes,dia,horaT,root.left)
            elif carnet>root.carnet:
                self.eliminar_T(carnet,posicion,año,mes,dia,horaT,root.right)

    def verTarea(self,carnet,posicion,año,mes,dia,horaT):
        if carnet<self.root.carnet:
            mensaje=self.ver_T(carnet,posicion,año,mes,dia,horaT,self.root.left)
        elif carnet>self.root.carnet:
            mensaje=self.ver_T(carnet,posicion,año,mes,dia,horaT,self.root.right)
        elif carnet==self.root.carnet:
            mensaje=self.root.años.verTarea(carnet,posicion,año,mes,dia,horaT)
        return mensaje  

    def ver_T(self,carnet,posicion,año,mes,dia,horaT,root):
        if root!=None:
            if carnet==root.carnet:
                mensaje=root.años.verTarea(posicion,año,mes,dia,horaT)
                return mensaje
            elif carnet<root.carnet:
                self.ver_T(carnet,posicion,año,mes,dia,horaT,root.left)
            elif carnet>root.carnet:
                self.ver_T(carnet,posicion,año,mes,dia,horaT,root.right)

    def graficaLT(self,carnet,año,mes,dia,hora):
        if carnet<self.root.carnet:
            mensaje=self.graficaLT_T(carnet,año,mes,dia,hora,self.root.left)
        elif carnet>self.root.carnet:
            mensaje=self.graficaLT_T(carnet,año,mes,dia,hora,self.root.right)
        elif carnet==self.root.carnet:
            mensaje=self.root.años.graficaLT(año,mes,dia,hora)
        return mensaje  

    def graficaLT_T(self,carnet,año,mes,dia,hora,root):
        if root!=None:
            if carnet==root.carnet:
                mensaje=root.años.graficaLT(año,mes,dia,hora)
                return mensaje
            elif carnet<root.carnet:
                self.graficaLT_T(carnet,año,mes,dia,hora,root.left)
            elif carnet>root.carnet:
                self.graficaLT_T(carnet,año,mes,dia,hora,root.right)   

    def graficaM(self,carnet,año,mes):
        if carnet<self.root.carnet:
            mensaje=self.graficaLM_T(carnet,año,mes,self.root.left)
        elif carnet>self.root.carnet:
            mensaje=self.graficaLM_T(carnet,año,mes,self.root.right)
        elif carnet==self.root.carnet:
            mensaje=self.root.años.graficaM(año,mes)
        return mensaje  

    def graficaLM_T(self,carnet,año,mes,root):
        if root!=None:
            if carnet==root.carnet:
                mensaje=root.años.graficaM(año,mes)
                return mensaje
            elif carnet<root.carnet:
                self.graficaLM_T(carnet,año,mes,root.left)
            elif carnet>root.carnet:
                self.graficaLM_T(carnet,año,mes,root.right)                  
       