#include <iostream>
using namespace std;

class NodoLD{
private:
    string carnet;
    string nombreTarea;
    string descripcion;
    string materia;
    string fecha;
    string hora;
    string estado;
    int id;
public:
    NodoLD *next;
    NodoLD *previous;
    NodoLD();
    NodoLD(string,string,string,string,string,string,string);
    string getCarnet();
    string getTarea();
    string getDescripcion();
    string getMateria();
    string getFecha();
    string getHora();
    string getEstado();
    int getId();
    void setCarnet(string);
    void setTarea(string);
    void setDescripcion(string);
    void setMateria(string);
    void setFecha(string);
    void setHora(string);
    void setEstado(string);
    void setId(int);
};
