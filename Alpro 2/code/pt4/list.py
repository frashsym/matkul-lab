print("=== MEMBUAT LIST ===")

contoh_list = [1, 2, 3, 4, 5]
print("Isi list:", contoh_list)

print("\n=== AKSES ELEMEN ===")

print("Elemen pertama:", contoh_list[0])
print("Elemen terakhir:", contoh_list[-1])

print("\n=== PANJANG LIST ===")

print("Jumlah elemen:", len(contoh_list))

print("\n=== AKSES DENGAN EKSPRESI ===")

print("Index 1+1:", contoh_list[1+1])

print("\n=== PERULANGAN LIST ===")

for elemen in contoh_list:
    print("Elemen:", elemen)

print("\n=== SLICING LIST ===")

print("contoh_list[1:4]:", contoh_list[1:4])
print("contoh_list[:4]:", contoh_list[:4])
print("contoh_list[1:]:", contoh_list[1:])

print("\n=== MENGUBAH ELEMEN ===")

contoh_list[0] = 10
print("Setelah diubah:", contoh_list)

print("\n=== MENAMBAH ELEMEN ===")

contoh_list.append(6)
print("Setelah append(6):", contoh_list)

contoh_list = contoh_list + [7]
print("Setelah + [7]:", contoh_list)

print("\n=== MENGHAPUS ELEMEN ===")

contoh_list.remove(3)
print("Setelah remove(3):", contoh_list)

elemen_dihapus = contoh_list.pop(1)
print("Setelah pop(1):", contoh_list)
print("Elemen yang dihapus:", elemen_dihapus)

print("\n=== POP TANPA INDEX ===")

last = contoh_list.pop()
print("Setelah pop():", contoh_list)
print("Elemen terakhir yang dihapus:", last)

print("\n=== CONTOH LIST CAMPURAN ===")

campur = [1, "dua", True, 4.5]
print("List campuran:", campur)