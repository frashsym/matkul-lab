"""Program pemesanan tiket kereta sederhana."""

# jumlah pesanan yang akan dibuat
try:
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan Tiket: "))
except ValueError:
    print("Input harus berupa angka. Program dihentikan.")
    exit()

# inisialisasi daftar
nama_pemesan = []
kode_kereta = []
kode_kelas = []
nama_kereta = []
nama_kelas = []
harga = []

for i in range(jumlah_pesanan):
    print(f"\nPesanan ke-{i+1}")
    nama = input("Masukkan Nama Pemesan: ").strip()
    nama_pemesan.append(nama)

    k_kereta = input("Masukkan Kode Kereta |CKR|MNR|: ").strip().upper()
    kode_kereta.append(k_kereta)

    k_kelas = input("Masukkan Kode Kelas |E|B|P|: ").strip().upper()
    kode_kelas.append(k_kelas)

    # tentukan nama kereta berdasarkan kode
    if k_kereta == "CKR":
        nama_kereta.append("Cakrabuana")
    elif k_kereta == "MNR":
        nama_kereta.append("Menoreh")
    else:
        nama_kereta.append("Tidak Diketahui")

    # tentukan kelas dan harga berdasarkan kereta dan kode kelas
    if k_kereta == "CKR":
        if k_kelas == "E":
            nama_kelas.append("Ekonomi")
            harga.append(45000)
        elif k_kelas == "B":
            nama_kelas.append("Bisnis")
            harga.append(80000)
        elif k_kelas == "P":
            nama_kelas.append("Premium")
            harga.append(100000)
        else:
            nama_kelas.append("Tidak Diketahui")
            harga.append(0)
    elif k_kereta == "MNR":
        if k_kelas == "E":
            nama_kelas.append("Ekonomi")
            harga.append(180000)
        elif k_kelas == "B":
            nama_kelas.append("Bisnis")
            harga.append(250000)  # asumsi harga
        elif k_kelas == "P":
            nama_kelas.append("Premium")
            harga.append(300000)  # asumsi harga
        else:
            nama_kelas.append("Tidak Diketahui")
            harga.append(0)
    else:
        # kereta tidak dikenali, beri harga 0
        if k_kelas == "E":
            nama_kelas.append("Ekonomi")
        elif k_kelas == "B":
            nama_kelas.append("Bisnis")
        elif k_kelas == "P":
            nama_kelas.append("Premium")
        else:
            nama_kelas.append("Tidak Diketahui")
        harga.append(0)

# tampilkan ringkasan pemesanan
print("\n=== RINGKASAN PESANAN ===")
total = 0
for idx in range(jumlah_pesanan):
    print(
        f"Pesanan {idx+1}: {nama_pemesan[idx]} - {nama_kereta[idx]} ({nama_kelas[idx]}) - Harga: Rp{harga[idx]}"
    )
    total += harga[idx]
print(f"\nTotal Bayar: Rp{total}")