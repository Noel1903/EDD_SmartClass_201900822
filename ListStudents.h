#include <iostream>
#include "NodoEstudiantes.h"
using namespace std;

class Lista{
    //private:

    public:
        Nodo *head=NULL;
        Nodo *last=NULL;
        void insertar(string,string,string,string,string,int,int,string);
        void agregar(string,string,string,string,string,int,int,string);
        int modificar(string);
        int eliminar(string);
        void mostar();
        void mostarInverso();
        int carnet(string);
        void corregir(string);
        void graficar();
        string reporte();
};
