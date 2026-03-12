#include <iostream>
#include <string>

using namespace std;

float menghitungGajiKaryawan() {
    string NIK, namaKaryawan, alamatKaryawan;
    int golongan, totalJamKerja, uangHarian, uangLembur, totalLembur, uangTransport, gapok, gajiTotal, pajak, gajiBersih;
    cout << "Masukkan NIK: ";
    cin >> NIK;
    cout << "Masukkan Nama Karyawan: ";
    cin >> namaKaryawan;
    cout << "Masukkan Alamat Karyawan: ";
    cin >> alamatKaryawan;
    cout << "Masukkan Golongan (1/2/3): ";
    cin >> golongan;
    cout << "Masukkan Total Jam Kerja: ";
    cin >> totalJamKerja;
    
    if (golongan == 1) {
        uangHarian = 20000;
        uangLembur = 10000;
        gapok = 3000000;
    } else if (golongan == 2) {
        uangHarian = 15000;
        uangLembur = 7500;
        gapok = 2500000;
    } else if (golongan == 3) {
        uangHarian = 10000;
        uangLembur = 5000;
        gapok = 2000000;
    }

    totalLembur = (totalJamKerja - 192) * uangLembur;
    uangTransport = uangHarian * 24;
    gajiTotal = gapok + uangTransport + totalLembur;
    pajak = 0.025 * gajiTotal;
    gajiBersih = gajiTotal - pajak;

    cout << "\n--- Rincian Gaji Karyawan ---\n";
    cout << "NIK: " << NIK << endl;
    cout << "Nama Karyawan: " << namaKaryawan << endl;
    cout << "Alamat Karyawan: " << alamatKaryawan << endl;
    cout << "Golongan: " << golongan << endl;
    cout << "Total Jam Kerja: " << totalJamKerja << endl;
    cout << "Gaji Pokok: " << gapok << endl;
    cout << "Uang Transport: " << uangTransport << endl;
    cout << "Total Lembur: " << totalLembur << endl;
    cout << "Gaji Total: " << gajiTotal << endl;
    cout << "Pajak: " << pajak<< endl;
    cout<<  "Gaji Bersih: "<< gajiBersih<<endl;

    return 0;

}

float menghitungKomisiSales(){
    string namaSales;
    int jumlahPenjualan, komisi;
    cout << "Masukkan Nama Sales: ";
    cin >> namaSales;
    cout << "Masukkan Total Penjualan: ";
    cin >> jumlahPenjualan;

    if (jumlahPenjualan > 1500000) {
        komisi = 0.15 * jumlahPenjualan;
    } else if (jumlahPenjualan > 1000000) {
        komisi = 0.125 * jumlahPenjualan;
    } else if (jumlahPenjualan >= 500000) {
        komisi = 0.10 * jumlahPenjualan;
    } else {
        komisi = 0;
    }

    cout << "\n--- Rincian Komisi Sales ---\n";
    cout << "Nama Sales: " << namaSales << endl;
    cout << "Jumlah Penjualan: " << jumlahPenjualan << endl;
    cout << "Komisi: " << komisi << endl;

    return 0;
}

void exit() {
    cout << "Terima kasih telah menggunakan program ini!" << endl;
    cout << "Keluar dari program..." << endl;
}

int main() {
    int pilihan;
    do {
        cout << "\n==========================================" << endl;
        cout << "Silahkan Pilih Sub-Program Yang akan Dijalankan:" << endl;
        cout << "1. Menghitung Gaji Karyawan" << endl;
        cout << "2. Menghitung Komisi Sales" << endl;
        cout << "3. Exit" << endl;
        cout << "Pilihan Anda (1/2/3): ";
        cin >> pilihan;

        switch (pilihan) {
            case 1: menghitungGajiKaryawan(); break;
            case 2: menghitungKomisiSales(); break;
            case 3: exit(); break;
            default: cout << "Pilihan tidak valid!" << endl;
        }
    } while (pilihan != 3);

    return 0;
}

// 1. Start
// 2. Input: NamaSales, JumlahPenjualan
// 3. Decision 1: Apakah JumlahPenjualan < 500.000?
// Ya: KomisiPenjualan = 0
// Tidak: Lanjut ke Decision 2

// 4. Decision 2: Apakah JumlahPenjualan <= 1.000.000?
// Ya: KomisiPenjualan = JumlahPenjualan * 10%
// Tidak: Lanjut ke Decision 3

// 5. Decision 3: Apakah JumlahPenjualan <= 1.500.000?
// Ya: KomisiPenjualan = JumlahPenjualan * 12.5%
// Tidak: KomisiPenjualan = JumlahPenjualan * 15%

// 6. Output: NamaSales, JumlahPenjualan, KomisiPenjualan
// 7. End