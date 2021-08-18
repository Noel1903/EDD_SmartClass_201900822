#include "ListaTareas.h"
ListaTareas::ListaTareas(){
    this->head=NULL;
    this->last=NULL;
}

ListaTareas::insertar(int _id,string _carnet,string _tarea,string _des,string _mat,string _fecha,string _hora,string _estado){
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
