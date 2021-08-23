#include "NodoLD.h"
NodoLD::NodoLD(){
    this->next=NULL;
    this->previous=NULL;
}
NodoLD::NodoLD(int _id,string _carnet,string _tarea,string _des,string _mat,string _fecha,string _hora,string _estado){
    this->id=_id;
    this->carnet=_carnet;
    this->nombreTarea=_tarea;
    this->descripcion=_des;
    this->materia=_mat;
    this->fecha=_fecha;
    this->hora=_hora;
    this->estado=_estado;
}
int NodoLD::getId(){
return this->id;
}
string NodoLD::getCarnet(){
return this->carnet;
}
string NodoLD:: getTarea(){
return this->nombreTarea;
}
string  NodoLD::getDescripcion(){
return this->descripcion;
}
string  NodoLD::getMateria(){
return this->materia;
}
string NodoLD:: getFecha(){return this->fecha;
}
string NodoLD:: getHora(){return this->hora;
}
string NodoLD:: getEstado(){return this->estado;
}
void NodoLD::setId(int _id){this->id=_id;}
void NodoLD::setCarnet(string carne){this->carnet=carne;}
void NodoLD::setTarea(string tarea){this->nombreTarea=tarea;}
void NodoLD::setDescripcion(string descrip){this->descripcion=descrip;}
void NodoLD::setMateria(string mat){this->materia=mat;}
void NodoLD::setFecha(string fech){this->fecha=fech;}
void NodoLD::setHora(string hour){this->hora=hour;}
void NodoLD::setEstado(string est){this->estado=est;}
