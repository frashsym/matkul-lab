# ==============================
# SISTEM DATA PRODUK TOKO
# ==============================

produk = [
    [1, "Buku", 10000, 20, "ATK"],
    [2, "Pulpen", 5000, 50, "ATK"],
    [3, "Pensil", 3000, 40, "ATK"],
    [4, "Penghapus", 2000, 30, "ATK"],
    [5, "Spidol", 8000, 25, "ATK"]
]

# AUTO ID
def generate_id():
    if len(produk) == 0:
        return 1
    return produk[-1][0] + 1


# TAMPIL DATA (TABEL RAPI)
def tampilkan_data():
    print("\n==================== DATA PRODUK ====================")
    print("{:<5} {:<15} {:<10} {:<10} {:<10}".format("ID", "Nama", "Harga", "Stok", "Kategori"))
    print("-"*53)
    
    for p in produk:
        print("{:<5} {:<15} {:<10} {:<10} {:<10}".format(p[0], p[1], p[2], p[3], p[4]))


# TAMBAH DATA
def tambah_data():
    print("\n=== TAMBAH DATA ===")
    
    id_baru = generate_id()
    print("ID otomatis:", id_baru)
    
    nama = input("Nama: ")
    
    try:
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
    except:
        print("Input harus angka!")
        return
    
    kategori = input("Kategori: ")
    
    produk.append([id_baru, nama, harga, stok, kategori])
    print("Data berhasil ditambahkan!")


# UBAH DATA
def ubah_data():
    tampilkan_data()
    
    try:
        id = int(input("Masukkan ID yang ingin diubah: "))
    except:
        print("ID harus angka!")
        return
    
    for p in produk:
        if p[0] == id:
            print("Kosongkan jika tidak ingin diubah")
            
            nama = input("Nama baru: ")
            if nama != "":
                p[1] = nama
            
            try:
                harga = input("Harga baru: ")
                if harga != "":
                    p[2] = int(harga)
                
                stok = input("Stok baru: ")
                if stok != "":
                    p[3] = int(stok)
            except:
                print("Input angka salah!")
                return
            
            kategori = input("Kategori baru: ")
            if kategori != "":
                p[4] = kategori
            
            print("Data berhasil diubah!")
            return
    
    print("Data tidak ditemukan!")


# HAPUS DATA
def hapus_data():
    tampilkan_data()
    
    try:
        id = int(input("Masukkan ID yang ingin dihapus: "))
    except:
        print("ID harus angka!")
        return
    
    for p in produk:
        if p[0] == id:
            produk.remove(p)
            print("Data berhasil dihapus!")
            return
    
    print("Data tidak ditemukan!")


# MENU UTAMA
def menu():
    while True:
        print("\n=== MENU TOKO ===")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")
        
        pilih = input("Pilih menu (1-5): ")
        
        if pilih == "1":
            tampilkan_data()
        elif pilih == "2":
            tambah_data()
        elif pilih == "3":
            ubah_data()
        elif pilih == "4":
            hapus_data()
        elif pilih == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


# JALANKAN
menu()