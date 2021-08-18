#include "ListaErrores.h"
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
