
#include "NodoEstudiantes.h"
Nodo::Nodo(){
    this->next=NULL;
    this->previous=NULL;
}

Nodo::Nodo(string _carnet,string _dpi,string _nombre,string _carrera,string _password,int _creditos,int _edad,string _correo){
    this->carnet=_carnet;
    this->dpi=_dpi;
    this->nombre=_nombre;
    this->carrera=_carrera;
    this->correo=_correo;
    this->password=_password;
    this->creditos=_creditos;
    this->edad=_edad;
}
string Nodo::getNombre(){
    return this->nombre;
}
string Nodo::getDpi(){
    return this->dpi;
}
string Nodo::getCarne(){
    return this->carnet;
}
string Nodo::getCarrera(){
    return this->carrera;
}
string Nodo::getCorreo(){
    return this->correo;
}
string Nodo::getPassword(){
    return this->password;
}
int Nodo::getCreditos(){
    return this->creditos;
}
int Nodo::getEdad(){
    return this->edad;
}
void Nodo::setDpi(string _dpi){
    this->dpi=_dpi;
}
void Nodo::setCarne(string _carne){
    this->carnet=_carne;
}
void Nodo::setNombre(string _nombre){
    this->nombre=_nombre;
}
void Nodo::setCarrera(string _carrera){
    this->carrera=_carrera;
}
void Nodo::setCorreo(string _correo){
    this->correo=_correo;
}
void Nodo::setPassword(string _password){
    this->password=_password;
}
void Nodo::setCreditos(int _creditos){
    this->creditos=_creditos;
}
void Nodo::setEdad(int _edad){
    this->edad=_edad;
}
