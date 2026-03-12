#include <iostream>
#include <string>
using namespace std;

int main()
{
    string nama, kelas;
    int nilai = 0;
    char huruf;

    cout << "Masukan Nama : ";
    getline(cin, nama);
    cout << "Masukan Kelas : ";
    getline(cin, kelas);
    cout << "Masukan Nilai : ";
    cin >> nilai;

    if (nilai > 85)
    {
        huruf = 'A';
    }
    else if (nilai > 75)
    {
        huruf = 'B';
    }
    else if (nilai > 65)
    {
        huruf = 'C';
    }
    else if (nilai > 45)
    {
        huruf = 'D';
    }
    else 
    {
        huruf = 'E';
    }

    cout << "Nama : " << nama << endl;
    cout << "Kelas : " << kelas << endl;
    cout << "Nilai : " << nilai << endl;
    cout << "Nilai berupa huruf : " << huruf << endl;
    return 0;
}
