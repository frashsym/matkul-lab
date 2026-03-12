
#include <iostream>
#include <string>
using namespace std;

// Struct Barang
struct Barang
{
    string nama;
    int harga;
    int jumlah;
};

int main()
{
    Barang daftarBarang[2];
    char lanjut = 'y';

    do
    {
        cout << "=== INPUT BARANG ===" << endl;

        for (int i = 0; i < 2; i++)
        { 
            cout << "\n--- Barang ke-" << (i + 1) << " ---" << endl;
            cout << "Nama barang: ";
            getline(cin, daftarBarang[i].nama);
            cout << "Harga: ";
            cin >> daftarBarang[i].harga;
            cout << "Jumlah: ";
            cin >> daftarBarang[i].jumlah;
            cin.ignore();
        }

        cout << "\n=== DAFTAR BARANG ===" << endl;
        for (int i = 0; i < 2; i++)
        {
            system("cls");
            cout << "Nama    : " << daftarBarang[i].nama << endl;
            cout << "Harga   : " << daftarBarang[i].harga << endl;
            cout << "Jumlah  : " << daftarBarang[i].jumlah << endl
                 << endl;
            cout << "Total Harga: " << daftarBarang[i].harga * daftarBarang[i].jumlah << endl;
        }
        cout << "\nApakah ingin input lagi? (y/n): ";
        cin >> lanjut;
        cin.ignore();
    } while (lanjut == 'y' || lanjut == 'Y');

    cout << "Terima kasih!" << endl;

    return 0;
}
