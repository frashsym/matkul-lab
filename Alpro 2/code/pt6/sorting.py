# def bubble_sort(arr):
#     n = len(arr)  # Mendapatkan panjang array (jumlah elemen)
#     for i in range(n):  # Loop luar: berjalan sebanyak n kali (untuk setiap elemen)
#         for j in range(0, n-i-1):  # Loop dalam: membandingkan elemen bersebelahan, mengurangi jangkauan setiap iterasi
#             if arr[j] > arr[j+1]:  # Jika elemen saat ini lebih besar dari elemen berikutnya
#                 arr[j], arr[j+1] = arr[j+1], arr[j]  # Tukar posisi kedua elemen
#     return arr  # Kembalikan array yang sudah diurutkan

# arr = [64, 34, 25, 12, 22, 11, 90]  # Array contoh yang belum diurutkan
# sorted_arr = bubble_sort(arr)  # Panggil fungsi bubble_sort dan simpan hasilnya
# print("Sorted array is:", sorted_arr)  # Cetak array yang sudah diurutkan

# Tambahan: urutkan 5 nama orang secara descending
names = ["Syahrul", "Raffi", "Athalla", "Dedria", "Alwi"]  # Daftar nama contoh

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Tukar jika elemen sekarang lebih kecil dari elemen berikutnya
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_names_desc = bubble_sort_desc(names)
print("Sorted names descending:", sorted_names_desc)  # Cetak nama yang sudah diurutkan dari Z ke A


