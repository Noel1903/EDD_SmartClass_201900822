
from flask import Flask,jsonify,Request
from flask.globals import request
app=Flask(__name__)

@app.route('/carga',methods=['POST'])
def cargaMasiva():
    
    tipo=request.json["tipo"]
    path=request.json["path"]
    return tipo

@app.route('/reporte',methods=['GET'])
def Reportes():
    datos=request.get_json()
    tipo=datos["tipo"]
    if tipo==0:
        return "AVL Estudiantes"
    elif tipo==1:
        carnet=datos["carnet"]
        año=datos["año"]
        mes=datos["mes"]
        return "Matriz de Tareas"
    elif tipo==2:
        carnet=datos["carnet"]
        año=datos["año"]
        mes=datos["mes"]
        dia=datos["dia"]
        hora=datos["hora"]
        return "Lista tareas"
    elif tipo==3:
        return "Arbol general de cursos"
    else:
        carnet=datos["carnet"]
        año=datos["año"]
        semestre=datos["semestre"]
        return "Arbol B de Cursos"

@app.route('/estudiante',methods=['POST','PUT','DELETE','GET'])
def estudiante():
    datos=request.get_json()
    if request.method=="POST":
        carnet=datos["carnet"]
        dpi=datos["DPI"]
        nombre=datos["nombre"]
        carrera=datos["carrera"]
        correo=datos["correo"]
        password=datos["password"]
        creditos=datos["creditos"]
        edad=datos["edad"]
        return "Crear usuario"
    elif request.method=="PUT":
        carnet=datos["carnet"]
        dpi=datos["DPI"]
        nombre=datos["nombre"]
        carrera=datos["carrera"]
        correo=datos["correo"]
        password=datos["password"]
        creditos=datos["creditos"]
        edad=datos["edad"]
        return "Modificar usuario"
    elif request.method=="GET":
        carnet=datos["carnet"]
        return "Ver usuario"
    else:
        carnet=datos["carnet"]
        return "Eliminar usuario"

        
if __name__=="__main__":
    app.run(port=3000,debug=True)