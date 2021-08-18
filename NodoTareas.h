#include <iostream>
using namespace std;
class NodoTareas{
private:
    string carnet;
    string nombreTarea;
    string descripcion;
    string materia;
    string fecha;
    string hora;
    string estado;

public:
    NodoTareas(string,string,string,string,string,string,string);
    string getcarnet();
    string getnombreT();
    string getDescripcion();
    string getMateria();
    string getFecha();
    string getHora();
    string getEstado();

};
