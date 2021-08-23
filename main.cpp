#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <regex>
#include "ListStudents.h"
#include "ListaErrores.h"
#include "NodoTareas.h"
#include "ListaTareas.h"
using namespace std;
Lista *nuevo=new Lista();
ListaE *err=new ListaE();
ListaTareas *tareas=new ListaTareas();
regex regcorr("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$");//Expresion regular del correo
regex regfecha("[0-9]{4}/((1[0-2])|(0[1-9]))/(([1-2][0-9])|0([1-9])|(3[0-1]))");//Expresion regular de la fecha
//Devuelve el index del mes
int indexMes(int M){
    switch(M){
        case 7:
            return 0;
        break;
        case 8:
            return 1;
        break;
        case 9:
            return 2;
        break;
        case 10:
            return 3;
        break;
        case 11:
            return 4;
        break;
        default:
            return -1;
        break;
    }
}
//Devuelve el index del dia
int indexDia(int D){
    if(D>0 & D<31){
        return D-1;
    }
    else{
        return -1;
    }

}
//Devuelve el index de la hora
int indexHora(int H){

    switch(H){
        case 8:
            return 0;
        break;
        case 9:
            return 1;
        break;
        case 10:
            return 2;
        break;
        case 11:
            return 3;
        break;
        case 12:
            return 4;
        break;
        case 13:
            return 5;
        break;
        case 14:
            return 6;
        break;
        case 15:
            return 7;
        break;
        case 16:
            return 8;
        break;
        default:
            return -1;
        break;
    }
}
//metodo para ingresar la tarea manualmente
void ingresarTarea(){
    int m,d,h;
    string carnet,nombre,descripcion,materia,fecha,estado;
    cout<<"Ingrese los datos de las tareas: (Mes,Dia,Hora,Carnet,Nombre,Descripcion,materia,fecha,estado)"<<endl;
    cin>>m;
    cin>>d;
    cin>>h;
    cin.ignore();
    getline(cin,carnet);
    getline(cin,nombre);
    getline(cin,descripcion);
    getline(cin,materia);
    getline(cin,fecha);
    getline(cin,estado);
    if(m>=7 & m<=11 & d>=1 & d<=30 &h>=8 & h<=16){
        tareas->ingreso(indexHora(h)+9*(indexDia(d)+30*indexMes(m)),carnet,nombre,descripcion,materia,fecha,to_string(h),estado);

    }else{
        err->insertar("Tarea","No esta en el rango valido","-1");
    }
}
//metodo para modificar la tarea manualmente
void modificarTarea(){
    int id;
    cout<<"Ingrese el id de la tarea que desea modificar"<<endl;
    cin>>id;
    tareas->modificar(id);

}
//metodo para eliminar la tarea manualmente
void eliminarTarea(){
    int id;
    cout<<"Ingrese el id de la tarea que desea eliminar"<<endl;
    cin>>id;
    tareas->eliminar(id);
}
//metodo para ingresar el usuario manualmente
void ingresarUsuario(){
    string carnet,dpi,nombre,carrera,correo,password;
    int creditos,edad;
    cout<<"Ingrese datos del nuevo usuario en orden:(Carnet,DPI,Nombre,Edad,Creditos,Carrera,Correo,Contraseña)"<<endl;
    cin.ignore();
    getline(cin,carnet);
    getline(cin,dpi);
    getline(cin,nombre);
    cin>>edad;
    cin>>creditos;
    cin.ignore();
    getline(cin,carrera);
    getline(cin,correo);
    getline(cin,password);
    nuevo->agregar(carnet,dpi,nombre,carrera,password,creditos,edad,correo);
    if(carnet.length()!=9){
        err->insertar("Estudiante","Carnet invalido",carnet);
    }
    if(dpi.length()!=13){
        err->insertar("Estudiante","DPI invalido",dpi);
    }
    if(!regex_match(correo,regcorr)){
        err->insertar("Estudiante","Correo invalido",correo);
    }

}
//metodo para modificar el usuario manualmente
void modificarUsuario(){
    string dpi;
    cout<<"Ingrese el dpi de la persona a modificar"<<endl;
    cin>>dpi;
    int res=nuevo->modificar(dpi);
    if(res==1){
        cout<<"Actualizado"<<endl;
    }else{
        cout<<"La persona no esta registrada"<<endl;
    }

}
//metodo para eliminar el usuario manualmente
void eliminarUsuario(){
    string dpi;
    cout<<"Ingrese el dpi de la persona a eliminar"<<endl;
    cin>>dpi;

    int res=nuevo->eliminar(dpi);
    if(res==1){
        cout<<"Eliminado"<<endl;
        nuevo->mostar();
    }else{
        cout<<"La persona no esta registrada"<<endl;
    }
}
void ingresoManual(){
    int op,opcion;
    cout<<"***************"<<endl;
    cout<<"1. Usuarios"<<endl;
    cout<<"2. Tareas"<<endl;
    cout<<"3. Salir"<<endl;
    cin>>op;
    switch(op){
        case 1:
            cout<<"***************"<<endl;
            cout<<"1. Ingresar"<<endl;
            cout<<"2. Modificar"<<endl;
            cout<<"3. Eliminar "<<endl;
            cout<<"4. Salir "<<endl;
            cin>>opcion;
            if(opcion==1){
                ingresarUsuario();
            }else if(opcion==2){
                modificarUsuario();
            }else if (opcion==3){
                eliminarUsuario();
            }

            break;
        case 2:
            cout<<"***************"<<endl;
            cout<<"1. Ingresar"<<endl;
            cout<<"2. Modificar"<<endl;
            cout<<"3. Eliminar "<<endl;
            cout<<"4. Salir "<<endl;
            cin>>opcion;
            if(opcion==1){
                ingresarTarea();
            }else if(opcion==2){
                modificarTarea();
            }else if (opcion==3){
                eliminarTarea();
            }

            break;
        case 3:
            break;
        default:
            break;
    }
}
//Funcion de Split para separar el ,
string *split(string texto){
    string *arreglo=new string[8];
    string cadena;
    char caracter=',';
    int c=0;

    for(int i=0;i<texto.length();i++){
        if(texto[i]!=caracter){
            cadena+=texto[i];
            if(i==texto.length()-1){
                arreglo[c]=cadena;
            }
        }
        else{
            arreglo[c]=cadena;
            c++;
            cadena="";
        }

    }
    return arreglo;
}
string *splitT(string texto){
    string *arreglo=new string[9];
    string cadena;
    char caracter=',';
    int c=0;

    for(int i=0;i<texto.length();i++){
        if(texto[i]!=caracter){
            cadena+=texto[i];
            if(i==texto.length()-1){
                arreglo[c]=cadena;
            }
        }
        else{
            arreglo[c]=cadena;
            c++;
            cadena="";
        }

    }
    return arreglo;
}
//Método para la carga masiva de usuarios
void CargaUsuarios(){

	string ruta,contenido;
	cout<<"Ingrese ruta del archivo de Usuarios:"<<endl;
	cin.ignore();

	getline(cin, ruta);
	ifstream archivo(ruta.c_str());
	int lineas=1,creditos,edad;
	char e[5],c[5];
	string *linea=new string[8];
	string dpi,carne,correo;
	if(archivo.fail()){
		cout<<"No se pudo abrir el archivo"<<endl;
	}else{
		while(!archivo.eof()){
			getline(archivo,contenido);

            if (lineas!=1 & contenido!=""){
                linea=split(contenido);
                strcpy(c,linea[5].c_str());
                strcpy(e,linea[6].c_str());
                carne=linea[0];
                dpi=linea[1];
                correo=linea[7];
                creditos=atoi(c);
                edad=atoi(e);
                nuevo->insertar(linea[0],linea[1],linea[2],linea[3],linea[4],creditos,edad,linea[7]);
                if(linea[0].length()!=9 & linea[0].length()!=0){
                    err->insertar("Estudiante","Error de carnet",carne);
                }
                if(linea[1].length()!=13 & linea[1].length()!=0){
                    err->insertar("Estudiante","Error de DPI",dpi);
                }
                if(regex_match(linea[7],regcorr)!=true & linea[7].length()!=0){
                    err->insertar("Estudiante","Error de correo",correo);
                }
            }
			lineas++;
		}
		archivo.close();
	}
	//nuevo->mostar();
	//err->mostrar();

}

void CargaTareas(){
    NodoTareas *matriz[5][30][9];
    for(int z=0;z<5;z++){
        for(int x=0;x<30;x++){
            for(int y=0;y<9;y++){
                matriz[z][x][y]=NULL;
            }
        }
    }
    string *linea=new string[9];
    int lineas=1;
    string ruta="",contenido;
    cout<<"Ingrese ruta del archivo de Tareas:"<<endl;
	cin.ignore();
	getline(cin, ruta);
	ifstream archivo(ruta.c_str());
    if(archivo.fail()){
        cout<<"No se pudo cargar el archivo"<<endl;
    }else{
        while(!archivo.eof()){
            getline(archivo,contenido);
            if (lineas!=1 & contenido!=""){
                linea=splitT(contenido);

                if(atoi(linea[0].c_str())>=7&atoi(linea[0].c_str())<=11){
                    if(atoi(linea[1].c_str())<=30 &atoi(linea[1].c_str())>=1){
                       if(atoi(linea[2].c_str())>=8 & atoi(linea[2].c_str())<=16){
                            if(!regex_match(linea[7],regfecha)){
                                err->insertar("Tarea","Formato YY/MM/DD erroneo",linea[7]);
                            }
                            if(nuevo->carnet(linea[3])!=1){
                                err->insertar("Tarea","Carnet no existe",linea[3]);
                            }
                            matriz[indexMes(atoi(linea[0].c_str()))][indexDia(atoi(linea[1].c_str()))][indexHora(atoi(linea[2].c_str()))]=new NodoTareas(linea[3],linea[4],linea[5],linea[6],linea[7],linea[2],linea[8]);

                        }else{
                            err->insertar("Tarea","Rango invalido de horario","");
                        }
                    }else{
                        err->insertar("Tarea","Rango invalido de horario","");
                     }
                }else{
                    err->insertar("Tarea","Rango invalido de horario","");
                }
            }
            lineas++;

        }
    }

    archivo.close();
    for(int z=0;z<=4;z++){
        for(int x=0;x<=29;x++){
            for(int y=0;y<=8;y++){
                if(matriz[z][x][y]!=NULL){
                    tareas->insertar(y+9*(x+30*z),matriz[z][x][y]->getcarnet(),matriz[z][x][y]->getnombreT(),matriz[z][x][y]->getDescripcion(),matriz[z][x][y]->getMateria(),matriz[z][x][y]->getFecha(),matriz[z][x][y]->getHora(),matriz[z][x][y]->getEstado());
                }
            }
        }
    }


}
//metodo de correccion de errores
void corregirErrores(){

    string dato=err->devolver()->getDato();
    string tipo=err->devolver()->getTipo();
    string descripcion=err->devolver()->getDescripcion();
    if(err->devolver()!=NULL ){
        cout<<descripcion<<endl;
        cout<<"Este dato es el incorrecto: "<<dato<<endl;
        if(tipo=="Estudiante"){
            nuevo->corregir(dato);
        }else{
            tareas->corregir(dato);
        }
        cout<<"Error Corregido"<<endl;
        err->desencolar();
    }else if(dato!=""){
        cout<<"Error Corregido"<<endl;
        err->desencolar();
    }else{
        cout<<"Nada que corregir"<<endl;
    }


}
//Metodo de devolver tarea
void devolverTarea(){
    int m,d,h,id;
    cout<<"Ingrese los datos(mes,dia,hora)"<<endl;
    cin>>m,
    cin>>d;
    cin>>h;
    if(indexHora(h)!=-1 & indexMes(m)!=-1 & indexDia(d)!=-1){
        id=indexHora(h)+9*(indexDia(d)+30*indexMes(m));
        tareas->devolverTarea(id);

    }else{
        cout<<"Datos fuera del rango establecido"<<endl;
    }

}
//metodo de devolver el id de una tarea
void indexTarea(){
    int m,d,h,id;
    cout<<"Ingrese los datos(mes,dia,hora)"<<endl;
    cin>>m,
    cin>>d;
    cin>>h;
    if(indexHora(h)!=-1 & indexMes(m)!=-1 & indexDia(d)!=-1){
        id=indexHora(h)+9*(indexDia(d)+30*indexMes(m));
        cout<<"En esta posicion deberia estar la tarea: "<<id<<endl;

    }else{
        cout<<"Datos fuera del rango establecido"<<endl;
    }

}
//Metodo para crear el documento de salida
void documento(){
    string document="";
    ofstream archivo;
    if(err->devolver()==NULL){
        document+="¿Elements?\n"+nuevo->reporte()+tareas->reporte()+" ¿$Elements?";
        archivo.open("Estudiantes.txt",ios::out);

        cout<<"Archivo creado correctamente"<<endl;
        if(archivo.fail()){
        cout<<"No se pudo crear el archivo"<<endl;
        }else{
            archivo<<document;
            archivo.close();
        }

    }else{
        cout<<"No se puede crear el documento, debe corregir errores"<<endl;
    }
}

int main(int argc, char** argv) {
    int op=0;

    try{
        while(op<=5){

            cout<<"Bienvenido a mi Smart Class"<<endl;
            cout<<"*******     Menu	*****"<<endl;
            cout<<"*	1.Carga de Usuarios	*"<<endl;
            cout<<"*	2.Carga de Tareas	*"<<endl;
            cout<<"*	3.Ingreso Manual	*"<<endl;
            cout<<"*	4.Corregir Errores	*"<<endl;
            cout<<"*	5.Reportes		*"<<endl;
            cout<<"Ingrese opcion:"<<endl;
            cin>>op;
            switch(op){
                case 1:
                    CargaUsuarios();
                    break;
                case 2:
                    CargaTareas();
                    break;
                case 3:
                    ingresoManual();
                    break;
                case 4:
                    corregirErrores();
                    break;
                case 5:
                    int opc=0;
                    cout<<"******************************"<<endl;
                    cout<<"1.Estudiantes"<<endl;
                    cout<<"2.Tareas"<<endl;
                    cout<<"3.Busqueda en estructura"<<endl;
                    cout<<"4.Busqueda en posicion"<<endl;
                    cout<<"5.Cola de Errores"<<endl;
                    cout<<"6.Codigo generado de salida"<<endl;
                    cin>>opc;
                    if(opc==1){
                        nuevo->graficar();
                    }else if(opc==2){
                        tareas->graficar();
                    }else if(opc==5){
                        err->graficar();
                    }else if(opc==3){
                        devolverTarea();
                    }else if(opc==4){
                        indexTarea();
                    }else if(opc==6){
                        documento();
                    }
                    break;
                }
            }
        }catch(...){
            cout<<"Ha realizado una accion invalida"<<endl;
        }



	return 0;
}

