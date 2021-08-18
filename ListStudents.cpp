#include <iostream>
#include "ListStudents.h"



void Lista::insertar(string carnet,string dpi,string nombre,string carrera,string password,int creditos,int edad,string correo){
    Nodo *nuevo=new Nodo(carnet,dpi,nombre,carrera,password,creditos,edad,correo);
    if (head==NULL){
        head=nuevo;
        last=nuevo;
        head->next=last;
        last->previous=head;
    }
    else{
        last->next=nuevo;
        nuevo->previous=last;
        last=nuevo;
        last->next=head;

    }

}
void Lista::agregar(string carnet,string dpi,string nombre,string carrera,string password,int creditos,int edad,string correo){
    Nodo *nuevo=new Nodo(carnet,dpi,nombre,carrera,password,creditos,edad,correo);
    if (head==NULL){
        head=nuevo;
        last=nuevo;
        head->next=last;
        last->previous=head;
    }
    else{
        last->next=nuevo;
        nuevo->previous=last;
        last=nuevo;
        last->next=head;
        head->previous=last;
    }
}

int Lista::modificar(string dpi){
    bool existe=false;
    Nodo *temp=head;
    string carnet,DPI,name,carr,corr;
    int cred,ed;
    while(temp){
        if(temp->getDpi()==dpi){
            cout<<"Datos de la persona"<<endl;
            cout<<"Carnet: "<<temp->getCarne()<<endl;
            cout<<"DPI: "<<temp->getDpi()<<endl;
            cout<<"Nombre: "<<temp->getNombre()<<endl;
            cout<<"Carrera: "<<temp->getCarrera()<<endl;
            cout<<"Correo: "<<temp->getCorreo()<<endl;
            cout<<"Creditos: "<<temp->getCreditos()<<endl;
            cout<<"Edad: "<<temp->getEdad()<<endl;
            cout<<"Ingrese los datos actualizados de la persona en el mismo orden"<<endl;
            cin>>carnet;
            cin>>DPI;
            cin>>name;
            cin>>carr;
            cin>>corr;
            cin>>cred;
            cin>>ed;
            temp->setCarne(carnet);temp->setDpi(DPI);temp->setNombre(name);temp->setCarrera(carr);
            temp->setCorreo(corr);temp->setCreditos(cred);temp->setEdad(ed);
            existe=true;
            break;
        }
        temp=temp->next;
        if(temp==head){
            break;

        }
    }
    if (existe){
        return 1;
    }
    else{
        return 0;
    }
}

int Lista::eliminar(string dpi){
    bool existe=false;
    Nodo *temp=head;
    string carnet,DPI,name,carr,corr;
    int cred,ed;
    while(temp){
        if(temp->getDpi()==dpi){
            if(temp==head){
                temp->next->previous=last;
                last->next=temp->next;
                head=temp->next;

            }
            else if(temp==last){
                temp->previous->next=head;
                head->previous=temp->previous;
                last=temp->previous;
            }
            else{
                temp->previous->next=temp->next;
                temp->next->previous=temp->previous;
            }
            existe=true;
            break;
        }
        temp=temp->next;
        if(temp==head){
            break;

        }
    }
    if (existe){
        return 1;
    }
    else{
        return 0;
    }
}




void Lista::mostar(){
    Nodo *temp=head;
    while(temp){
        cout<<temp->getNombre()<<endl;
        cout<<temp->getDpi()<<endl;
        cout<<temp->getCarne()<<endl;
        temp=temp->next;
        if(temp==head){
            break;
        }
    }
}
void Lista::mostarInverso(){
    Nodo *temp=last;
    while(temp){
        cout<<temp->getNombre()<<endl;
        cout<<temp->getDpi()<<endl;
        cout<<temp->getCarne()<<endl;
        temp=temp->previous;
        if(temp==head){
            cout<<temp->getNombre()<<endl;
            cout<<temp->getDpi()<<endl;
            cout<<temp->getCarne()<<endl;
            break;
        }
    }
}
