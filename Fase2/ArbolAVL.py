from listaAños import ListaAños

class Hoja:
    def __init__(self,alumnos):
        self.alumnos=alumnos
        self.años=None
        self.left=None
        self.right=None
        self.height=0

class Arbol:
    def __init__(self):
        self.root=None

    def max(self,n1,n2):
        return max(n1,n2)

    def height(self,root):
        if root!=None:
            return root.height
        return -1

    def insertar(self,carnet,año):
        self.root=self.insertarHoja(carnet,año,self.root)
        
    def insertarHoja(self,carnet,año,root):
        if root==None:
            nuevo=Hoja(carnet)
            anios=ListaAños()
            nuevo.años=anios
            anios.insertar(año)
            return nuevo
        elif carnet>root.alumnos:
           root.right=self.insertarHoja(carnet,año,root.right)
           if self.height(root.right)-self.height(root.left)==2:
                if carnet<root.right.alumnos:
                   root=self.Doble_rotD(root)
                else:
                    root=self.rotacionI(root)
        elif carnet<root.alumnos:
            root.left=self.insertarHoja(carnet,año,root.left)
        else:
            root.años.insertar(año)
        root.height=self.max(self.height(root.left),self.height(root.right))+1

        return root
    

    def rotacionD(self,root):
        temp=root.left
        root.right=temp.left
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
        return root

    def mostrar(self):
        nodo=self.root
        print(nodo.alumnos)
        nodo.años.mostrar()
        print(nodo.left.alumnos)
        nodo.left.años.mostrar()
        print(nodo.right.alumnos)
        nodo.right.años.mostrar()