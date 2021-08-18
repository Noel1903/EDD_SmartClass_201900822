#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <regex>
#include "ListStudents.h"
#include "ListaErrores.h"

using namespace std;
Lista *nuevo=new Lista();
ListaE *err=new ListaE();
regex regcorr("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$");
void ingresarUsuario(){

}
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
    int op;
    cout<<"1. Usuarios"<<endl;
    cout<<"2. Tareas"<<endl;
    cout<<"3. Salir"<<endl;
    cin>>op;
    switch(op){
        case 1:
            int opcion;
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

            if (lineas!=1 & lineas!=NULL){
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
	err->mostrar();

}

void CargaTareas(){
    string ruta="";
    cout<<"Ingrese ruta del archivo de Usuarios:"<<endl;
	cin.ignore();
	getline(cin, ruta);
	ifstream archivo(ruta.c_str());
    if(archivo.fail()){
        cout<<"No se pudo cargar el archivo"<<endl;
    }else{

    }
}



int main(int argc, char** argv) {
    int op=0;
    while(op<=4){
        cout<<"Bienvenido a mi Smart Class"<<endl;
        cout<<"*******     Menu	*****"<<endl;
        cout<<"*	1.Carga de Usuarios	*"<<endl;
        cout<<"*	2.Carga de Tareas	*"<<endl;
        cout<<"*	3.Ingreso Manual	*"<<endl;
        cout<<"*	4.Reportes		*"<<endl;
        cout<<"Ingrese opcion:"<<endl;
        cin>>op;
        switch(op){
            case 1:
                CargaUsuarios();
                break;
            case 2:
                break;
            case 3:
                ingresoManual();
                break;
            case 4:
                break;
            default:
                cout<<"No ha escogido ninguna opcion"<<endl;
                break;
        }

    }


	return 0;
}

