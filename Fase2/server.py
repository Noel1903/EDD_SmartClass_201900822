from flask import Flask,jsonify,Request
from flask.globals import request
from PLY.main import Analizador
from ArbolAVL import Arbol
analisis=Analizador()
datos=Arbol()
app=Flask(__name__)
@app.route('/carga',methods=['POST'])
def cargaMasiva():
    tipo=request.json["tipo"]
    if tipo=="1":
        path=request.json["path"]
        datas=analisis.analisis(path,tipo)
        for data in datas:
            datos.insertar(data["Carnet"],data["Dpi"],data["Nombre"],data["Carrera"],data["Correo"],data["Password"],data["Creditos"],data["Edad"])
        datos.imprimir()
    elif tipo=="2":
        path=request.json["path"]
        datas=analisis.analisis(path,tipo)
        for data in datas:
            fecha=data["Fecha"].split("/")
            año=fecha[2]
            mes=fecha[1]
            dia=fecha[0]
            hora=data["Hora"].split(":")
            datos.insertarAño(data["Carnet"],año,mes,dia,hora[0],data["Nombre"],data["Descripcion"],data["Materia"],data["Fecha"],data["Hora"],data["Estado"])
        #datos.mostrarA()       
    return tipo


@app.route('/reporte',methods=['GET'])
def Reportes():
    data=request.get_json()
    tipo=data["tipo"]
    if tipo==0:
        datos.graficarArbol()
        return "AVL Estudiantes"
    elif tipo==1:
        carnet=data["carnet"]
        año=data["año"]
        mes=str(data["mes"])
        if len(mes)==1:
            Mes="0"+mes
        else:
            Mes=mes
        datos.graficaM(carnet,año,Mes)
        return "Matriz de Tareas"
    elif tipo==2:
        carnet=data["carnet"]
        año=data["año"]
        mes=str(data["mes"])
        dia=str(data["dia"])
        hora=data["hora"]
        if len(mes)==1:
            Mes="0"+mes
        else:
            Mes=mes
        if len(dia)==1:
            Dia="0"+dia
        else:
            Dia=dia
        datos.graficaLT(carnet,año,Mes,Dia,str(hora))
        return "Lista tareas"
    elif tipo==3:
        return "Arbol general de cursos"
    elif tipo==4:
        carnet=data["carnet"]
        año=data["año"]
        semestre=data["semestre"]
        return "Arbol B de Cursos"

@app.route('/estudiante',methods=['POST','PUT','DELETE','GET'])
def estudiante():
    data=request.get_json()
    if request.method=="POST":
        carnet=data["carnet"]
        dpi=data["DPI"]
        nombre=data["nombre"]
        carrera=data["carrera"]
        correo=data["correo"]
        password=data["password"]
        creditos=data["creditos"]
        edad=data["edad"]
        datos.insertar(carnet,dpi,nombre,carrera,correo,password,creditos,edad)
        return "Crear usuario"
    elif request.method=="PUT":
        carnet=data["carnet"]
        dpi=data["DPI"]
        nombre=data["nombre"]
        carrera=data["carrera"]
        correo=data["correo"]
        password=data["password"]
        creditos=data["creditos"]
        edad=data["edad"]
        mensaje=datos.modificar(carnet,dpi,nombre,carrera,correo,password,creditos,edad)
        return mensaje
    elif request.method=="GET":
        carnet=data["carnet"]
        mensaje=datos.mostrarEstudiante(carnet)
        return mensaje
    else:
        carnet=data["carnet"]
        return "Eliminar usuario"

@app.route('/recordatorios',methods=['POST','PUT','DELETE','GET'])
def recordatorio():
    data=request.get_json()
    if request.method=="POST":
        fecha=data["Fecha"].split("/")
        año=fecha[2]
        mes=fecha[1]
        dia=fecha[0]
        hora=data["Hora"].split(":")
        datos.insertarAño(data["Carnet"],año,mes,dia,hora[0],data["Nombre"],data["Descripcion"],data["Materia"],data["Fecha"],data["Hora"],data["Estado"])
        return "Tarea creada correctamente"
    elif request.method=="PUT":
        carnet=data["Carnet"]
        nombre=data["Nombre"]
        descripcion=data["Descripcion"]
        materia=data["Materia"]
        fecha=data["Fecha"]
        hora=data["Hora"]
        estado=data["Estado"]
        posicion=data["Posicion"]
        datoFecha=data["Fecha"].split("/")
        año=datoFecha[2]
        mes=datoFecha[1]
        dia=datoFecha[0]
        datoHora=data["Hora"].split(":")
        horaT=datoHora[0]
        datos.modificarTarea(carnet,nombre,descripcion,materia,fecha,hora,estado,posicion,año,mes,dia,horaT)
        return "Modificar tarea"
    elif request.method=="GET":
        carnet=data["Carnet"]
        fecha=data["Fecha"]
        hora=data["Hora"]
        posicion=data["Posicion"]
        datoFecha=data["Fecha"].split("/")
        año=datoFecha[2]
        mes=datoFecha[1]
        dia=datoFecha[0]
        datoHora=data["Hora"].split(":")
        horaT=datoHora[0]
        mensaje=datos.verTarea(carnet,posicion,año,mes,dia,horaT)
        return mensaje
    elif request.method=="DELETE":
        carnet=data["Carnet"]
        fecha=data["Fecha"]
        hora=data["Hora"]
        posicion=data["Posicion"]
        datoFecha=data["Fecha"].split("/")
        año=datoFecha[2]
        mes=datoFecha[1]
        dia=datoFecha[0]
        datoHora=data["Hora"].split(":")
        horaT=datoHora[0]
        datos.eliminarT(carnet,posicion,año,mes,dia,horaT)
        return "Eliminar Tarea"

if __name__=="__main__":
    app.run(port=3000,debug=True,host='0.0.0.0')