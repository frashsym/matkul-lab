# Membuat Variabel
nama_pemesanan = []
kode_kereta = []
nama_kereta = []
kode_kelas = []
nama_kelas = []
harga = []

# Pengkondisian dan Perulangan
jumlah_pesanan = int(input("Masukkan Jumlah Pesanan Tiket : "))
for i in range(jumlah_pesanan):
    print("Pesanan Ke-", i + 1)
    nama_pemesanan.append(input("Masukkan Nama Pemesanan : "))
    kode_kereta.append(input("Masukkan Kode Kereta |CKR|MNR| : "))
    kode_kelas.append(input("Masukkan Kode Kelas |E|B|P| : "))
    if kode_kereta[i] == "CKR" or kode_kereta[i] == "ckr":
        nama_kereta.append("Cakrabuana")
        if kode_kelas[i] == "E" or kode_kelas[i] == "e":
            nama_kelas.append("Ekonomi")
            harga.append(int(45000))
        elif kode_kelas[i] == "B" or kode_kelas[i] == "b":
            nama_kelas.append("Bisnis")
            harga.append(int(80000))
        elif kode_kelas[i] == "P" or kode_kelas[i] == "p":
            nama_kelas.append("Premium")
            harga.append(int(100000))
        else:
            nama_kelas.append("kosong")
            harga.append(int(0))
    elif kode_kereta[i] == "MNR" or kode_kereta[i] == "mnr":
        nama_kereta.append("Menoreh")
        if kode_kelas[i] == "E" or kode_kelas[i] == "e":
            nama_kelas.append("Ekonomi")
            harga.append(int(100000))
        elif kode_kelas[i] == "B" or kode_kelas[i] == "b":
            nama_kelas.append("Bisnis")
            harga.append(int(220000))
        elif kode_kelas[i] == "P" or kode_kelas[i] == "p":
            nama_kelas.append("Premium")
            harga.append(int(360000))
        else:
            nama_kelas.append("kosong")
            harga.append(int(0))
    else:
        nama_kereta.append("Tidak Ada")
        if kode_kelas[i] == "E" or kode_kelas[i] == "e":
            nama_kelas.append("Ekonomi")
            harga.append(int(100000))
        elif kode_kelas[i] == "B" or kode_kelas[i] == "b":
            nama_kelas.append("Bisnis")
            harga.append(int(220000))
        elif kode_kelas[i] == "P" or kode_kelas[i] == "p":
            nama_kelas.append("Premium")
            harga.append(int(360000))
        else:
            nama_kelas.append("kosong")
            harga.append(int(0))

# Perhitungan
total = sum(harga)
if total > 200000:
    diskon = 10 / 100 * total
else:
    diskon = 0
bayar = total - diskon

#Output / Keluaran

import pandas as pd

data={

}

Nama:nama_pemesan,

'Kereta:nama_kereta,

"Kelas': nama_kelas,

"Harga: harga

rekap data-pd.DataFrame(data)

print("-"*50)

print("PROGRAM PEMESANAN TIKET KERETA")

print("-"*50)

print(rekap_data)

print("-"*50)

print("Total Pesanan\t=", total)

print("Diskon\t=", diskon)

print("Total Bayar\t=", bayar)

uang_bayar-int(input("Masukkan Uang Bayar\t="))

kembalian uang_bayar-bayar

print("Kembalian\t=", kembalian)

print(""*50)

# # Tampilkan Ringkasan Pesanan
# print("\n=== RINGKASAN PESANAN ===")
# for idx in range(jumlah_pesanan):
#     print(f"Pesanan {idx+1}: {nama_pemesanan[idx]} - {nama_kereta[idx]} ({nama_kelas[idx]}) - Rp{harga[idx]}")


# # Tampilkan Total
# print(f"\nTotal Harga: Rp{total}")
# print(f"Diskon (10% jika >200000): Rp{int(diskon)}")
# print(f"Total Bayar: Rp{int(bayar)}")
