#include <iostream>

using namespace std;

class NodoE{
    private:
        int id;
        string tipo;
        string descripcion;
        string dato;
    public:
        NodoE *next;
        NodoE();
        NodoE(int,string,string,string);
        string getTipo();
        string getDescripcion();
        string getDato();
        int getId();
};
