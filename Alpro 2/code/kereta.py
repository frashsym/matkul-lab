import datetime

class Kereta:
    def __init__(self, id_kereta, nama, asal, tujuan, total_kursi, harga):
        self.id_kereta = id_kereta
        self.nama = nama
        self.asal = asal
        self.tujuan = tujuan
        self.total_kursi = total_kursi
        self.kursi_tersedia = total_kursi
        self.harga = harga

    def tampilkan_info(self):
        return f"ID: {self.id_kereta} | {self.nama} | {self.asal} -> {self.tujuan} | Kursi: {self.kursi_tersedia}/{self.total_kursi} | Harga: Rp{self.harga}"

class Pemesanan:
    def __init__(self, id_pemesanan, penumpang, kereta, jumlah_kursi, tanggal):
        self.id_pemesanan = id_pemesanan
        self.penumpang = penumpang
        self.kereta = kereta
        self.jumlah_kursi = jumlah_kursi
        self.tanggal = tanggal
        self.total_harga = kereta.harga * jumlah_kursi

    def tampilkan_info(self):
        return f"ID Pemesanan: {self.id_pemesanan} | Penumpang: {self.penumpang} | Kereta: {self.kereta.nama} | Kursi: {self.jumlah_kursi} | Total: Rp{self.total_harga} | Tanggal: {self.tanggal}"

class SistemPemesanan:
    def __init__(self):
        self.kereta_list = []
        self.pemesanan_list = []
        self.id_pemesanan_counter = 1
        self.inisialisasi_kereta()

    def inisialisasi_kereta(self):
        # Menambahkan beberapa kereta contoh
        self.kereta_list.append(Kereta("K001", "Argo Bromo", "Jakarta", "Surabaya", 100, 250000))
        self.kereta_list.append(Kereta("K002", "Gajayana", "Jakarta", "Malang", 80, 200000))
        self.kereta_list.append(Kereta("K003", "Taksaka", "Bandung", "Yogyakarta", 120, 180000))
        self.kereta_list.append(Kereta("K004", "Mutiara Selatan", "Jakarta", "Bandung", 150, 50000))

    def tampilkan_kereta_tersedia(self):
        print("\n=== KERETA YANG TERSEDIA ===")
        for kereta in self.kereta_list:
            if kereta.kursi_tersedia > 0:
                print(kereta.tampilkan_info())

    def cari_kereta(self, asal, tujuan):
        hasil = []
        for kereta in self.kereta_list:
            if kereta.asal.lower() == asal.lower() and kereta.tujuan.lower() == tujuan.lower() and kereta.kursi_tersedia > 0:
                hasil.append(kereta)
        return hasil

    def pesan_tiket(self, nama_penumpang, id_kereta, jumlah_kursi):
        kereta = None
        for k in self.kereta_list:
            if k.id_kereta == id_kereta:
                kereta = k
                break

        if kereta is None:
            print("Kereta tidak ditemukan!")
            return False

        if kereta.kursi_tersedia < jumlah_kursi:
            print(f"Kursi tidak cukup! Tersedia: {kereta.kursi_tersedia}")
            return False

        # Kurangi kursi tersedia
        kereta.kursi_tersedia -= jumlah_kursi

        # Buat pemesanan
        tanggal = datetime.date.today().strftime("%Y-%m-%d")
        pemesanan = Pemesanan(self.id_pemesanan_counter, nama_penumpang, kereta, jumlah_kursi, tanggal)
        self.pemesanan_list.append(pemesanan)
        self.id_pemesanan_counter += 1

        print(f"\nPemesanan berhasil!")
        print(pemesanan.tampilkan_info())
        return True

    def batalkan_pemesanan(self, id_pemesanan):
        pemesanan = None
        for p in self.pemesanan_list:
            if p.id_pemesanan == id_pemesanan:
                pemesanan = p
                break

        if pemesanan is None:
            print("Pemesanan tidak ditemukan!")
            return False

        # Kembalikan kursi
        pemesanan.kereta.kursi_tersedia += pemesanan.jumlah_kursi

        # Hapus pemesanan
        self.pemesanan_list.remove(pemesanan)

        print(f"Pemesanan {id_pemesanan} berhasil dibatalkan!")
        return True

    def tampilkan_pemesanan(self):
        if not self.pemesanan_list:
            print("\nBelum ada pemesanan.")
            return

        print("\n=== DAFTAR PEMESANAN ===")
        for pemesanan in self.pemesanan_list:
            print(pemesanan.tampilkan_info())

def menu_utama():
    sistem = SistemPemesanan()

    while True:
        print("\n" + "="*50)
        print("     SISTEM PEMESANAN TIKET KERETA API")
        print("="*50)
        print("1. Lihat Kereta Tersedia")
        print("2. Cari Kereta")
        print("3. Pesan Tiket")
        print("4. Batalkan Pemesanan")
        print("5. Lihat Pemesanan Saya")
        print("6. Keluar")
        print("="*50)

        try:
            pilihan = int(input("Pilih menu (1-6): "))

            if pilihan == 1:
                sistem.tampilkan_kereta_tersedia()

            elif pilihan == 2:
                asal = input("Masukkan kota asal: ")
                tujuan = input("Masukkan kota tujuan: ")
                hasil_cari = sistem.cari_kereta(asal, tujuan)
                if hasil_cari:
                    print(f"\nKereta dari {asal} ke {tujuan}:")
                    for kereta in hasil_cari:
                        print(kereta.tampilkan_info())
                else:
                    print(f"Tidak ada kereta dari {asal} ke {tujuan}.")

            elif pilihan == 3:
                sistem.tampilkan_kereta_tersedia()
                id_kereta = input("\nMasukkan ID kereta: ")
                nama_penumpang = input("Masukkan nama penumpang: ")
                try:
                    jumlah_kursi = int(input("Masukkan jumlah kursi: "))
                    sistem.pesan_tiket(nama_penumpang, id_kereta, jumlah_kursi)
                except ValueError:
                    print("Jumlah kursi harus berupa angka!")

            elif pilihan == 4:
                sistem.tampilkan_pemesanan()
                try:
                    id_pemesanan = int(input("\nMasukkan ID pemesanan yang akan dibatalkan: "))
                    sistem.batalkan_pemesanan(id_pemesanan)
                except ValueError:
                    print("ID pemesanan harus berupa angka!")

            elif pilihan == 5:
                sistem.tampilkan_pemesanan()

            elif pilihan == 6:
                print("Terima kasih telah menggunakan sistem pemesanan tiket kereta!")
                break

            else:
                print("Pilihan tidak valid!")

        except ValueError:
            print("Masukkan angka yang valid!")

        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    menu_utama()
