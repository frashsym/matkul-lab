# ==============================
# PROGRAM TOKO (LIST 2 DIMENSI)
# ==============================

# Data awal (matriks 5x5)
produk = [
    [1, "Pensil", 2000, 50, "ATK"],
    [2, "Buku", 5000, 30, "ATK"],
    [3, "Penghapus", 1000, 40, "ATK"],
    [4, "Pulpen", 3000, 25, "ATK"],
    [5, "Spidol", 7000, 20, "ATK"]
]

# ==============================
# FUNCTION TAMPILKAN DATA
# ==============================
def tampilkan_data():
    print("\n=== DATA PRODUK ===")
    print("ID | Nama | Harga | Stok | Kategori")
    for p in produk:
        print(p[0], "|", p[1], "|", p[2], "|", p[3], "|", p[4])

# ==============================
# FUNCTION TAMBAH DATA
# ==============================
def tambah_data():
    print("\n=== TAMBAH DATA ===")
    id = int(input("Masukkan ID: "))
    nama = input("Masukkan Nama: ")
    harga = int(input("Masukkan Harga: "))
    stok = int(input("Masukkan Stok: "))
    kategori = input("Masukkan Kategori: ")

    produk.append([id, nama, harga, stok, kategori])
    print("Data berhasil ditambahkan!")

# ==============================
# FUNCTION UBAH DATA
# ==============================
def ubah_data():
    print("\n=== UBAH DATA ===")
    id = int(input("Masukkan ID yang ingin diubah: "))

    for p in produk:
        if p[0] == id:
            print("Data ditemukan!")
            p[1] = input("Nama baru: ")
            p[2] = int(input("Harga baru: "))
            p[3] = int(input("Stok baru: "))
            p[4] = input("Kategori baru: ")
            print("Data berhasil diubah!")
            return

    print("Data tidak ditemukan!")

# ==============================
# FUNCTION HAPUS DATA
# ==============================
def hapus_data():
    print("\n=== HAPUS DATA ===")
    id = int(input("Masukkan ID yang ingin dihapus: "))

    for p in produk:
        if p[0] == id:
            produk.remove(p)
            print("Data berhasil dihapus!")
            return

    print("Data tidak ditemukan!")

# ==============================
# MENU UTAMA
# ==============================
def menu():
    while True:
        print("\n=== MENU TOKO ===")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Program selesai!")
            break
        else:
            print("Pilihan tidak valid!")

# ==============================
# JALANKAN PROGRAM
# ==============================
menu()