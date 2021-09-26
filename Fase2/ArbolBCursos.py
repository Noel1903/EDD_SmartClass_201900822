class Nodo:
    def __init__(self,codigo,nombre,creditos,prerequisitos,tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.creditos=creditos
        self.prerequisitos=prerequisitos
        self.tipo=tipo
        self.auxI=None
        self.auxD=None

    def getNombre(self):
        return self.nombre

class ArbolB:
    def __init__(self):
        self.root=[]
        self.child=[]
        self.arriba=False
        self.cont=0
        


    def insertar(self,codigo,nombre,creditos,prerequisitos,tipo):
        self.root=self.insertar01(codigo,nombre,creditos,prerequisitos,tipo,self.root)


    def insertar01(self,codigo,nombre,creditos,prerequisitos,tipo,root):
        nuevo=Nodo(codigo,nombre,creditos,prerequisitos,tipo)
        root.append(nuevo)
        arr=sorted(root,key=lambda nuevo:nuevo.codigo)
        self.cont+=1
        if self.cont<5:
            return arr
        else:
            root.append(nuevo)
            arr=sorted(root,key=lambda nuevo:nuevo.codigo)
            root=self.romper(arr)
            return root


    def romper(self,root):
        self.arriba=True
        self.child.append(root[0])
        self.child.append(root[1])
        root.auxI=self.child
        self.child=[]
        self.child.append(root[3])
        self.child.append(root[4])
        root.auxD=self.child
        return root[2]



    def mostrar(self):
        self.mostrar1(self.root)

    def mostrar1(self,root):
        for i in root:
            print(i.getNombre())
        self.mostrar1(self,root.auxI)
        self.mostrar1(self,root.auxD)