#include "NodoTareas.h"

NodoTareas::NodoTareas(string _carnet,string _nombreTarea,string _descripcion,string _materia,string _fecha,string _hora,string _estado){
    this->carnet=_carnet;
    this->nombreTarea=_nombreTarea;
    this->descripcion=_descripcion;
    this->materia=_materia;
    this->fecha=_fecha;
    this->hora=_hora;
    this->estado=_estado;
}

string NodoTareas::getcarnet(){
    return this->carnet;
}
string NodoTareas::getnombreT(){
    return this->nombreTarea;
}
string NodoTareas::getDescripcion(){
    return this->descripcion;
}
string NodoTareas::getMateria(){
    return this->materia;
}
string NodoTareas::getFecha(){
    return this->fecha;
}
string NodoTareas::getHora(){
    return this->hora;
}
string NodoTareas::getEstado(){
    return this->estado;
}

