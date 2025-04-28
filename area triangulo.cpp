#include <iostream>
using namespace std;

int main() {
    float a, e;
    float l;
    cout << "Ingrese la base del triangulo: ";
    cin >> a;
    cout << "Ingrese la altura del triangulo: ";
    cin >> e;
    l = (a*e)/2;
    cout << "La area del triangulo es de: " << l << endl;

    return 0;
}
