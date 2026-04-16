print("\n=== LATIHAN 1 ===")

latihan1 = [1, 2, 3, 4, 5]
print("3 elemen pertama (manual):", latihan1[0], latihan1[1], latihan1[2])
print("3 elemen pertama (slicing):", latihan1[:3])

latihan1.append(6)
print("Setelah tambah 6:", latihan1)

latihan1.remove(3)
print("Setelah hapus 3:", latihan1)

latihan1.pop()
print("Setelah hapus terakhir:", latihan1)

print("Panjang list:", len(latihan1))

print("\n=== LATIHAN 2 ===")

buah = ["Apple", "Lychee", "Mango", "Banana", "Berry"]
print("List buah:", buah)

buah.append("Honeydew")
buah.append("Passion Fruit")
print("Setelah tambah buah:", buah)

buah.remove("Lychee")
print("Setelah hapus Lychee:", buah)

buah.pop()
print("Setelah hapus terakhir:", buah)

print("Panjang list:", len(buah))

print("\n=== LATIHAN 3 ===")

def buku():
    daftar_buku = [
        "Laskar Pelangi",
        "Panduan Shalat",
        "Programming Python",
        "Ekonomi Mikro",
        "Pemrograman Visual",
    ]

    print("Daftar Buku:")
    for i in range(len(daftar_buku)):
        print(f"{i+1}. {daftar_buku[i]}")

    # daftar_buku.append("Harry Potter")
    # daftar_buku.append("The Lord of the Rings")

    # print("\nSetelah tambah buku:")
    # for i in range(len(daftar_buku)):
    #     print(f"{i+1}. {daftar_buku[i]}")

buku()


# === LATIHAN DI RUMAH ===
# 1. Buatlah daftar buku pakai function
# 2. Tambahkan buku dengan inputan user
# 3. Tampilkan daftar buku setelah ditambahkan
# 4. Tampilkan jumlah buku yang ada di daftar

def latihan_rumah():
    daftar_buku = [
        "Laskar Pelangi",
        "Panduan Shalat",
        "Programming Python",
        "Ekonomi Mikro",
        "Pemrograman Visual"
    ]
    
    # Tambahkan buku dengan inputan user
    while True:
        tambah = input("Masukkan nama buku baru (atau 'stop' untuk berhenti): ")
        if tambah.lower() == 'stop':
            break
        daftar_buku.append(tambah)
    
    # Tampilkan daftar buku setelah ditambahkan
    print("\nDaftar Buku Setelah Ditambahkan:")
    for i in range(len(daftar_buku)):
        print(f"{i+1}. {daftar_buku[i]}")
    
    # Tampilkan jumlah buku
    print(f"\nJumlah buku yang ada di daftar: {len(daftar_buku)}")

latihan_rumah()