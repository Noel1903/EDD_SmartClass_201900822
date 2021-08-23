#include "NodoLD.h"

class ListaTareas{
public:
    NodoLD *head;
    NodoLD *last;
    ListaTareas();
    void insertar(int _id,string _carnet,string _tarea,string _des,string _mat,string _fecha,string _hora,string _estado);
    void ingreso(int _id,string _carnet,string _tarea,string _des,string _mat,string _fecha,string _hora,string _estado);
    void modificar(int index);
    void eliminar(int index);
    void mostrar();
    void corregir(string);
    void graficar();
    void devolverTarea(int);
    string invertir(string);
    string reporte();
};
