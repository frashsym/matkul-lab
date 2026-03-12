#include <iostream>
using namespace std;

// fungsi hitung luas persegi panjang (tanpa parameter)
void luas_persegi_panjang(){
    float p, l;
    cout << "\n=== Luas Persegi Panjang ===\n";
    cout << "Masukkan panjang : ";
    cin >> p;
    cout << "Masukkan lebar   : ";
    cin >> l;

    float luas = p * l;
    cout << "Luas persegi panjang = " << luas << endl;
}

// fungsi hitung luas lingkaran (tanpa parameter)
void luas_lingkaran(){
    float r;
    const float phi = 3.14;

    cout << "\n=== Luas Lingkaran ===\n";
    cout << "Masukkan jari-jari : ";
    cin >> r;

    float luas = phi * r * r;
    cout << "Luas lingkaran = " << luas << endl;
}

// fungsi hitung luas segitiga (tanpa parameter)
void luas_segitiga(){
    float a, t;

    cout << "\n=== Luas Segitiga ===\n";
    cout << "Masukkan alas  : ";
    cin >> a;
    cout << "Masukkan tinggi: ";
    cin >> t;

    float luas = 0.5 * a * t;
    cout << "Luas segitiga = " << luas << endl;
}

int main(){
    // memanggil ketiga fungsi
    luas_persegi_panjang();
    luas_lingkaran();
    luas_segitiga();

    return 0;
}