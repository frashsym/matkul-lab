#include <iostream>
using namespace std;

struct Mahasiswa
{
    string nim, nama;
    int nt, uts, uas;
    float na;
    char nh;
};

int main()
{
    char ulang = 'y';

    do
    {
        system("cls");
        cout << "\nData Mahasiswa";
        Mahasiswa mhs[3];
        
        for (int i = 0; i < 3; i++)
        {
            cout << "\nNIM  : ";
            cin >> mhs[i].nim;
            cout << "Nama : ";
            cin.ignore();
            getline(cin, mhs[i].nama);
            cout << "Nilai Tugas : ";
            cin >> mhs[i].nt;
            cout << "Nilai UTS : ";
            cin >> mhs[i].uts;
            cout << "Nilai UAS : ";
            cin >> mhs[i].uas;

            mhs[i].na = (mhs[i].nt * 0.15) + (mhs[i].uts * 0.35) + (mhs[i].uas * 0.50);

            if (mhs[i].na >= 80)
                mhs[i].nh = 'A';
            else if (mhs[i].na >= 75)
                mhs[i].nh = 'B';
            else if (mhs[i].na >= 60)
                mhs[i].nh = 'C';
            else if (mhs[i].na >= 45)
                mhs[i].nh = 'D';
            else
                mhs[i].nh = 'E';
        }

        cout << "\n=== Data Mahasiswa ===" << endl;
        for (int i = 0; i < 3; i++)
        {
            cout << "\nMahasiswa ke-" << i + 1 << endl;
            cout << "NIM          : " << mhs[i].nim << endl;
            cout << "Nama         : " << mhs[i].nama << endl;
            cout << "Nilai Tugas  : " << mhs[i].nt << endl;
            cout << "Nilai UTS    : " << mhs[i].uts << endl;
            cout << "Nilai UAS    : " << mhs[i].uas << endl;
            cout << "Nilai Akhir  : " << mhs[i].na << endl;
            cout << "Nilai Huruf  : " << mhs[i].nh << endl;
        }

        cout << "\nApakah Anda ingin mengulang? (y/n): ";
        cin >> ulang;
        if (ulang != 'y' && ulang != 'Y')
        {
            cout << "Terima kasih!" << endl;
        }
    } while (ulang == 'y' || ulang == 'Y');

    return 0;
}