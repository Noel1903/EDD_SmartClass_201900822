#include "NodoErrores.h"

class ListaE{
    public:
        NodoE *head;
        NodoE *last;
        ListaE();
        void insertar(string,string,string);
        void mostrar();
        void desencolar();
        NodoE *devolver();
        int cont=0;
        void graficar();
};
