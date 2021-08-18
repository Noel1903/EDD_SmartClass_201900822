#include <iostream>
#include <string>
using namespace std;
class Nodo{
    private:
        string carnet;
        string dpi;
        string nombre;
        string carrera;
        string correo;
        string password;
        int creditos;
        int edad;


    public:
        Nodo *next;
        Nodo *previous;
        Nodo();

        Nodo(string,string,string,string,string,int,int,string);
        string getCarne();
        string getNombre();
        string getDpi();
        string getCarrera();
        string getCorreo();
        string getPassword();
        int getCreditos();
        int getEdad();
        void setCarne(string);
        void setDpi(string);
        void setNombre(string);
        void setCarrera(string);
        void setCorreo(string);
        void setPassword(string);
        void setCreditos(int);
        void setEdad(int);

};

