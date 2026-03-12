
#include <iostream>
#include <string>
using namespace std;

// Struct Mahasiswa
struct Mahasiswa {
    string nama;
    string nim;
    string jurusan;
    float ipk;
};

int main()
{
    int jumlah;
    
    cout << "Berapa jumlah mahasiswa yang ingin diinput? ";
    cin >> jumlah;
    cin.ignore(); // Membersihkan buffer
    
    // Membuat array of struct
    Mahasiswa mhs[jumlah];
    
    // Input data mahasiswa
    for (int i = 0; i < jumlah; i++) {
        cout << "\n--- Data Mahasiswa ke-" << (i + 1) << " ---" << endl;
        cout << "Nama   : ";
        getline(cin, mhs[i].nama);
        cout << "NIM    : ";
        getline(cin, mhs[i].nim);
        cout << "Jurusan: ";
        getline(cin, mhs[i].jurusan);
        cout << "IPK    : ";
        cin >> mhs[i].ipk;
        cin.ignore();
    }
    
    // Menampilkan semua data mahasiswa
    cout << "\n========== DAFTAR MAHASISWA ==========" << endl;
    for (int i = 0; i < jumlah; i++) {
        cout << "\nMahasiswa " << (i + 1) << ":" << endl;
        cout << "Nama    : " << mhs[i].nama << endl;
        cout << "NIM     : " << mhs[i].nim << endl;
        cout << "Jurusan : " << mhs[i].jurusan << endl;
        cout << "IPK     : " << mhs[i].ipk << endl;
    }
    
    return 0;
}
