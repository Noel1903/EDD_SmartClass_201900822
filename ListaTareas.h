#include "NodoLD.h"
class ListaTareas{
public:
    NodoLD *head;
    NodoLD *last;
    ListaTareas();
    void insertar(int _id,string _carnet,string _tarea,string _des,string _mat,string _fecha,string _hora,string _estado);
};
