#include <iostream>
#include <fstream>
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
            cin.ignore();
            getline(cin,carnet);
            getline(cin,DPI);
            getline(cin,name);
            getline(cin,carr);
            getline(cin,corr);
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
int Lista::carnet(string _carnet){
    int existe=0;
    Nodo *temp=head;
    while(temp){
        if(_carnet==temp->getCarne()){
            existe=1;
            break;
        }
        temp=temp->next;
        if(temp==head){break;}
    }
    return existe;
}
void Lista::corregir(string dato){
    string nuevo_dato;
    Nodo *temp=head;
    while(temp){
        if(temp->getCarne()==dato){
            cout<<"Ingrese el carnet correcto"<<endl;
            cin>>nuevo_dato;
            temp->setCarne(nuevo_dato);
            break;
        }
        if(temp->getDpi()==dato){
            cout<<"Ingrese el DPI correcto"<<endl;
            cin>>nuevo_dato;
            temp->setDpi(nuevo_dato);
            break;
        }
        if(temp->getCorreo()==dato){
            cout<<"Ingrese el correo correcto"<<endl;
            cin>>nuevo_dato;
            temp->setCorreo(nuevo_dato);
            break;
        }
        temp=temp->next;
        if(temp==head){break;}
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
void Lista::graficar(){
    ofstream archivo;

    string contenido="";
    int c=1;
    Nodo *temp=head;
    while(temp){
        if(temp->getDpi()!=""){
            contenido+=to_string(c)+"[label=\"Carnet:"+temp->getCarne()+"\\nDPI:"+temp->getDpi()+"\\nNombre:"+temp->getNombre()+"\\nCorreo:"+temp->getCorreo()+"\\nCarrera:"+temp->getCarrera()+"\\nCreditos:"+to_string(temp->getCreditos())+"\"]\n";
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
            contenido+=to_string(c-1)+"->"+to_string(1);
        }else{
            contenido+=to_string(i)+"->";
        }
    }

    string documento="digraph G{ \nrankdir=LR \n  node[shape=box]\n edge[dir=both];\n "+contenido+"   \n }";
    archivo.open("ListaAlumnos.dot",ios::out);
    if(archivo.fail()){
        cout<<"No se pudo crear el archivo"<<endl;
    }else{
        archivo<<documento;
        archivo.close();
        cout<<"Archivo creado correctamente"<<endl;
        system("dot -Tpdf ListaAlumnos.dot -o ListaAlumnos.pdf");
    }


}
string Lista::reporte(){
    string report="";
    Nodo *temp=head;
    while(temp){
        report+="¿element type=\"user\"?\n";
        report+="¿item Carnet=\""+temp->getCarne()+"\" $?\n";
        report+="¿item DPI=\""+temp->getDpi()+"\" $?\n";
        report+="¿item Nombre=\""+temp->getNombre()+"\" $?\n";
        report+="¿item Carrera=\""+temp->getCarrera()+"\" $?\n";
        report+="¿item Password=\""+temp->getPassword()+"\" $?\n";
        report+="¿item Creditos=\""+to_string(temp->getCreditos())+"\" $?\n";
        report+="¿item Edad=\""+to_string(temp->getEdad())+"\" $?\n";
        report+="¿$element?\n";
        temp=temp->next;
        if(temp==head){
            break;
        }
    }
    return report;
}
