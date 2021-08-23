#include "ListaErrores.h"
#include <iostream>
#include <fstream>
ListaE::ListaE(){
this->head=NULL;
this->last=NULL;
}
void ListaE::insertar(string _tipo,string _descripcion,string _dato){
    this->cont++;
    NodoE *nuevo=new NodoE(cont,_tipo,_descripcion,_dato);
    if(this->head==NULL){
        head=nuevo;
        last=nuevo;
        last->next=NULL;
        head->next=NULL;
    }
    else{
        last->next=nuevo;
        last=nuevo;
        last->next=NULL;
    }
}
void ListaE::desencolar(){
    NodoE *temp=head;
    if(head){
        head=temp->next;
    }
    else{
        cout<<"No hay nada mas que corregir"<<endl;
    }

}
NodoE* ListaE::devolver(){
    NodoE *temp=head;
    return temp;
}

void ListaE::mostrar(){
    NodoE *temp=head;
    while(temp){
        cout<<"Id: "<<temp->getId()<<" Tipo: "<<temp->getTipo()<<" Descripcion: "<<temp->getDescripcion()<<" Error: "<<temp->getDato()<<endl;
        temp=temp->next;
        if(temp==last){
            break;
        }
    }
}

void ListaE::graficar(){
    ofstream archivo;
    string contenido="";
    int c=1;
    NodoE *temp=head;
    while(temp){
        if(temp->getDescripcion()!=""){
            contenido+=to_string(c)+"[label=\"Id:"+to_string(temp->getId())+"\\nDescripcion:"+temp->getDescripcion()+"\\nTipo:"+temp->getTipo()+"\"]\n";
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

    string documento="digraph G{ \nrankdir=LR \n  node[shape=box]\n "+contenido+"   \n }";
    archivo.open("ListaErrores.dot",ios::out);
    if(archivo.fail()){
        cout<<"No se pudo crear el archivo"<<endl;
    }else{
        archivo<<documento;
        archivo.close();
        cout<<"Archivo creado correctamente"<<endl;
        system("dot -Tpdf ListaErrores.dot -o ListaErrores.pdf");
    }


}

