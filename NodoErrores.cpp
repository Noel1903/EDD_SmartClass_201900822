#include "NodoErrores.h"

NodoE::NodoE(){
    this->next=NULL;
}
NodoE::NodoE(int _id,string _tipo,string _descripcion,string _dato){
    this->id=_id;
    this->tipo=_tipo;
    this->descripcion=_descripcion;
    this->dato=_dato;
}
string NodoE::getDato(){
    return this->dato;
}
string NodoE::getDescripcion(){
    return this->descripcion;
}
string NodoE::getTipo(){
    return this->tipo;
}
int NodoE::getId(){
    return this->id;
}
