#include "ListaTareas.h"
#include <iostream>
#include <fstream>
using namespace std;
ListaTareas::ListaTareas(){
    this->head=NULL;
    this->last=NULL;
}

void ListaTareas::insertar(int _id,string _carnet,string _tarea,string _des,string _mat,string _fecha,string _hora,string _estado){
    NodoLD *nuevo=new NodoLD(_id,_carnet,_tarea,_des,_mat,_fecha,_hora,_estado);
    if(head==NULL){
        head=nuevo;
        last=nuevo;
    }
    else{
        last->next=nuevo;
        nuevo->previous=last;
        last=nuevo;
        last->next=NULL;
    }

}
void ListaTareas::ingreso(int _id,string _carnet,string _tarea,string _des,string _mat,string _fecha,string _hora,string _estado){
    int existe=0;
    NodoLD *temp=head;
    while(temp){
        if(temp->getId()==_id){
            existe=1;
            break;
        }
        temp=temp->next;
    }
    temp=head->next;
    if(existe){
        cout<<"El id ya esta ocupado"<<endl;
    }else{
        NodoLD *nuevo=new NodoLD(_id,_carnet,_tarea,_des,_mat,_fecha,_hora,_estado);
        if(_id<head->getId()){
            nuevo->next=head;
            head->previous=nuevo;
            head=nuevo;
        }
        else if(_id>last->getId()){
            insertar(_id,_carnet,_tarea,_des,_mat,_fecha,_hora,_estado);
        }
        else{
            while(temp){
                if(temp->getId()<_id & temp->next->getId()>_id){
                    temp->next->previous=nuevo;
                    nuevo->next=temp->next;
                    temp->next=nuevo;
                    nuevo->previous=temp;
                    break;
                }


                temp=temp->next;
                if(temp==last){
                    break;
                }
            }
        }


        cout<<"Ingresado"<<endl;
    }
}
void ListaTareas::modificar(int index){
    string carn,nom,des,mat,fech,est;
    int existe=0;
    NodoLD *temp=head;
    while(temp){
        if(temp->getId()==index){
            cout<<"Ingrese los datos nuevos"<<endl;
            cout<<"Carnet: "<<endl;cin.ignore();getline(cin,carn);
            cout<<"Nombre tarea: "<<endl;cin.ignore();getline(cin,nom);
            cout<<"Descripcion: "<<endl;cin.ignore();getline(cin,des);
            cout<<"Materia: "<<endl;cin.ignore();getline(cin,mat);
            cout<<"Fecha: "<<endl;cin.ignore();getline(cin,fech);
            cout<<"Estado: "<<endl;cin.ignore();getline(cin,est);
            temp->setCarnet(carn);
            temp->setTarea(nom);
            temp->setDescripcion(des);
            temp->setMateria(mat);
            temp->setFecha(fech);
            temp->setEstado(est);

            existe=1;
            break;
        }
        temp=temp->next;
    }
    if(existe){
        cout<<"Datos actualizados correctamente"<<endl;
    }else{
        cout<<"El id no existe"<<endl;
    }
}

void ListaTareas::eliminar(int index){
    NodoLD *temp=head;
    int existe=0;
    while(temp){
        if(temp->getId()==index){
            temp->setCarnet("-1");
            temp->setTarea("-1");
            temp->setDescripcion("-1");
            temp->setMateria("-1");
            temp->setFecha("-1");
            temp->setEstado("-1");
            temp->setHora("-1");
            existe=1;
            break;
        }
        temp=temp->next;
    }
    if(existe){
        cout<<"Datos eliminados correctamente"<<endl;
    }else{
        cout<<"El id que ingreso no existe"<<endl;
    }
}
void ListaTareas::corregir(string dato){
    string nuevo_dato;
    NodoLD *temp=head;
    while(temp){
        if(temp->getCarnet()==dato){
            cout<<"Ingrese el carnet correcto"<<endl;
            cin>>nuevo_dato;
            temp->setCarnet(nuevo_dato);
            break;
        }
        if(temp->getFecha()==dato){
            cout<<"Ingrese la fecha de formato correcto"<<endl;
            cin>>nuevo_dato;
            temp->setFecha(nuevo_dato);
            break;
        }
        temp=temp->next;
    }
}
void ListaTareas::mostrar(){
    NodoLD *temp=head;
    while(temp){

        cout<<"Materia: "<<temp->getMateria()<<" Estado: "<<temp->getEstado()<<endl;
        temp=temp->next;
    }
}
void ListaTareas::graficar(){
    ofstream archivo;
    string contenido="";
    int c=1;
    NodoLD *temp=head;
    while(temp){
        if(temp->getCarnet()!=""){
            contenido+=to_string(c)+"[label=\"Carnet:"+temp->getCarnet()+"\\nNombre:"+temp->getTarea()+"\\nDescripcion:"+temp->getDescripcion()+"\\nMateria:"+temp->getMateria()+"\\nFecha:"+temp->getFecha()+"\\nHora:"+temp->getHora()+":00\\nEstado:"+temp->getEstado()+"\"]\n";
            c++;
        }

        temp=temp->next;
        if(temp==head){
            break;
        }
    }
    for(int i=1;i<=c-1;i++){
        if(i==c-1){
            contenido+=to_string(i)+";\n";
        }else{
            contenido+=to_string(i)+"->";
        }
    }

    string documento="digraph G{ \nrankdir=LR \n  node[shape=box]\n edge[dir=both];\n "+contenido+"   \n }";
    archivo.open("ListaTareas.dot",ios::out);
    if(archivo.fail()){
        cout<<"No se pudo crear el archivo"<<endl;
    }else{
        archivo<<documento;
        archivo.close();
        cout<<"Archivo creado correctamente"<<endl;
        system("dot -Tpdf ListaTareas.dot -o ListaTareas.pdf");
    }


}

void ListaTareas::devolverTarea(int index){
    NodoLD *temp;
    int existe=0;
    while(temp){
        if(index==temp->getId()){
            existe=1;
            cout<<"Carnet: "<<temp->getCarnet()<<endl;
            cout<<"Nombre: "<<temp->getTarea()<<endl;
            cout<<"Descripcion: "<<temp->getDescripcion()<<endl;
            cout<<"Materia: "<<temp->getMateria()<<endl;
            cout<<"Fecha: "<<temp->getFecha()<<endl;
            cout<<"Hora: "<<temp->getHora()<<":00"<<endl;
            cout<<"Estado: "<<temp->getEstado()<<endl;
        }
        temp=temp->next;
    }
    if(existe==0){
        cout<<"Esta tarea no existe"<<endl;
    }
}
string ListaTareas::invertir(string fecha){
    int c=0;
    string fechai="",acum="";
    string *text=new string [3];
    for(int i=0;i<fecha.length();i++){
        if(fecha[i]!='/'){
            acum+=fecha[i];
            if(i==fecha.length()-1){
                text[c]=acum;
            }
        }else{
            text[c]=acum;
            c++;
            acum="";
        }
    }
    for(int i=2;i>=0;i--){
        if(i!=0){
           fechai+=text[i]+"/";

        }else{
            fechai+=text[i];
        }

    }

    return fechai;
}
string ListaTareas::reporte(){
    string report="";
    NodoLD *temp=head;
    while(temp){
        report+="¿element type=\"task\"?\n";
        report+="¿item Carnet=\""+temp->getCarnet()+"\" $?\n";
        report+="¿item Nombre=\""+temp->getTarea()+"\" $?\n";
        report+="¿item Descripcion=\""+temp->getDescripcion()+"\" $?\n";
        report+="¿item Materia=\""+temp->getMateria()+"\" $?\n";
        report+="¿item Fecha=\""+invertir(temp->getFecha())+"\" $?\n";
        report+="¿item Hora=\""+temp->getHora()+":00\" $?\n";
        report+="¿item Estado=\""+temp->getEstado()+"\" $?\n";
        report+="¿$element?\n";
        temp=temp->next;
    }
    return report;
}
