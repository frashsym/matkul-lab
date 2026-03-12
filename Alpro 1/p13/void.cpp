#include <iostream>
using namespace std;

void say_hello(string name)
{
    cout << "Hello, " << name << "!" << endl;
}

int main()
{
    string name;
    cout << "Masukan Nama: ";
    getline(cin, name);
    say_hello(name);
    return 0;
}