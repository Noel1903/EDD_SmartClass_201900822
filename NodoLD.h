#include <iostream>
#include <string>
using namespace std;

class NodoLD{
private:
    int id;
    string carnet;
    string nombreTarea;
    string descripcion;
    string materia;
    string fecha;
    string hora;
    string estado;
public:
    NodoLD *next;
    NodoLD *previous;
    NodoLD();
    NodoLD(int,string,string,string,string,string,string,string);
    int getId();
    string getCarnet();
    string getTarea();
    string getDescripcion();
    string getMateria();
    string getFecha();
    string getHora();
    string getEstado();
    void setId(int);
    void setCarnet(string);
    void setTarea(string);
    void setDescripcion(string);
    void setMateria(string);
    void setFecha(string);
    void setHora(string);
    void setEstado(string);
};
