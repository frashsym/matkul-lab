#include <iostream>
using namespace std;

float luasPersegi()
{
    float p, l;
    cout << "Masukan Panjang Persegi: ";
    cin >> p;
    cout << "Masukan Lebar Persegi: ";
    cin >> l;
    return p * l;
}

float luasLingkaran()
{
    float r;
    cout << "Masukan Jari-jari Lingkaran: ";
    cin >> r;
    return 3.14 * r * r;
}

float luasSegitiga()
{
    float a, t;
    cout << "Masukan Alas Segitiga: ";
    cin >> a;
    cout << "Masukan Tinggi Segitiga: ";
    cin >> t;
    return 0.5 * a * t;
}

void menu()
{
    cout << "\n=== MENU ===" << endl;
    cout << "1. Luas Persegi" << endl;
    cout << "2. Luas Lingkaran" << endl;
    cout << "3. Luas Segitiga" << endl;
    cout << "Pilih menu (1-3): ";
}

int main()
{
    int pilihan;
    float hasil;

    menu();
    cin >> pilihan;

    switch (pilihan)
    {
        case 1:
            hasil = luasPersegi();
            cout << "Luas Persegi: " << hasil << endl;
            break;

        case 2:
            hasil = luasLingkaran();
            cout << "Luas Lingkaran: " << hasil << endl;
            break;

        case 3:
            hasil = luasSegitiga();
            cout << "Luas Segitiga: " << hasil << endl;
            break;

        default:
            cout << "Pilihan tidak valid!" << endl;
    }

    return 0;
}
