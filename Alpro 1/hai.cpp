#include <iostream>
using namespace std;

struct Hai {
    char nama[30];
    int umur;
    char hobi[50];
};

int main() {
    Hai orang; // membuat variabel orang dari struct Hai

    cout << "Nama: ";
    cin.getline(orang.nama, 30);

    cout << "Umur: ";
    cin >> orang.umur;
    cin.ignore(); // membersihkan newline dari buffer

    cout << "Hobi: ";
    cin.getline(orang.hobi, 50);

    cout << "\n=== Data Hai ===";
    cout << "\nNama: " << orang.nama;
    cout << "\nUmur: " << orang.umur;
    cout << "\nHobi: " << orang.hobi;

    return 0;
}