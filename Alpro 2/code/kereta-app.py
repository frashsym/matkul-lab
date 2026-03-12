import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog


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
        self.kereta_list.append(
            Kereta("K001", "Argo Bromo", "Jakarta", "Surabaya", 100, 250000)
        )
        self.kereta_list.append(
            Kereta("K002", "Gajayana", "Jakarta", "Malang", 80, 200000)
        )
        self.kereta_list.append(
            Kereta("K003", "Taksaka", "Bandung", "Yogyakarta", 120, 180000)
        )
        self.kereta_list.append(
            Kereta("K004", "Mutiara Selatan", "Jakarta", "Bandung", 150, 50000)
        )

    def tampilkan_kereta_tersedia(self):
        print("\n=== KERETA YANG TERSEDIA ===")
        for kereta in self.kereta_list:
            if kereta.kursi_tersedia > 0:
                print(kereta.tampilkan_info())

    def cari_kereta(self, asal, tujuan):
        hasil = []
        for kereta in self.kereta_list:
            if (
                kereta.asal.lower() == asal.lower()
                and kereta.tujuan.lower() == tujuan.lower()
                and kereta.kursi_tersedia > 0
            ):
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
        pemesanan = Pemesanan(
            self.id_pemesanan_counter, nama_penumpang, kereta, jumlah_kursi, tanggal
        )
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


class GUISistemPemesanan:
    def __init__(self, root):
        self.sistem = SistemPemesanan()
        self.root = root
        self.root.title("Sistem Pemesanan Tiket Kereta API")
        self.root.geometry("600x500")

        # Text area untuk output
        self.output_text = tk.Text(root, height=15, width=70)
        self.output_text.pack(pady=10)

        # Frame untuk button
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Button untuk setiap menu
        tk.Button(button_frame, text="Lihat Kereta Tersedia", command=self.lihat_kereta).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cari Kereta", command=self.cari_kereta).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Pesan Tiket", command=self.pesan_tiket).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Batalkan Pemesanan", command=self.batalkan_pemesanan).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Lihat Pemesanan", command=self.lihat_pemesanan).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Keluar", command=root.quit).pack(side=tk.LEFT, padx=5)

        # Tampilkan pesan selamat datang
        self.output_text.insert(tk.END, "Selamat datang di Sistem Pemesanan Tiket Kereta API!\n\n")

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

    def lihat_kereta(self):
        self.clear_output()
        self.output_text.insert(tk.END, "=== KERETA YANG TERSEDIA ===\n")
        for kereta in self.sistem.kereta_list:
            if kereta.kursi_tersedia > 0:
                self.output_text.insert(tk.END, kereta.tampilkan_info() + "\n")

    def cari_kereta(self):
        asal = simpledialog.askstring("Cari Kereta", "Masukkan kota asal:")
        if not asal:
            return
        tujuan = simpledialog.askstring("Cari Kereta", "Masukkan kota tujuan:")
        if not tujuan:
            return

        hasil_cari = self.sistem.cari_kereta(asal, tujuan)
        self.clear_output()
        if hasil_cari:
            self.output_text.insert(tk.END, f"Kereta dari {asal} ke {tujuan}:\n")
            for kereta in hasil_cari:
                self.output_text.insert(tk.END, kereta.tampilkan_info() + "\n")
        else:
            self.output_text.insert(tk.END, f"Tidak ada kereta dari {asal} ke {tujuan}.\n")

    def pesan_tiket(self):
        # Tampilkan kereta dulu
        self.lihat_kereta()
        
        id_kereta = simpledialog.askstring("Pesan Tiket", "Masukkan ID kereta:")
        if not id_kereta:
            return
        nama_penumpang = simpledialog.askstring("Pesan Tiket", "Masukkan nama penumpang:")
        if not nama_penumpang:
            return
        jumlah_kursi_str = simpledialog.askstring("Pesan Tiket", "Masukkan jumlah kursi:")
        if not jumlah_kursi_str:
            return
        
        try:
            jumlah_kursi = int(jumlah_kursi_str)
            success = self.sistem.pesan_tiket(nama_penumpang, id_kereta, jumlah_kursi)
            self.clear_output()
            if success:
                self.output_text.insert(tk.END, "Pemesanan berhasil!\n")
                # Refresh tampilan kereta
                self.lihat_kereta()
            else:
                self.output_text.insert(tk.END, "Pemesanan gagal. Periksa input Anda.\n")
        except ValueError:
            messagebox.showerror("Error", "Jumlah kursi harus berupa angka!")

    def batalkan_pemesanan(self):
        # Tampilkan pemesanan dulu
        self.lihat_pemesanan()
        
        id_pemesanan_str = simpledialog.askstring("Batalkan Pemesanan", "Masukkan ID pemesanan:")
        if not id_pemesanan_str:
            return
        
        try:
            id_pemesanan = int(id_pemesanan_str)
            success = self.sistem.batalkan_pemesanan(id_pemesanan)
            self.clear_output()
            if success:
                self.output_text.insert(tk.END, f"Pemesanan {id_pemesanan} berhasil dibatalkan!\n")
                # Refresh tampilan kereta
                self.lihat_kereta()
            else:
                self.output_text.insert(tk.END, "Pembatalan gagal. Periksa ID pemesanan.\n")
        except ValueError:
            messagebox.showerror("Error", "ID pemesanan harus berupa angka!")

    def lihat_pemesanan(self):
        self.clear_output()
        if not self.sistem.pemesanan_list:
            self.output_text.insert(tk.END, "Belum ada pemesanan.\n")
            return

        self.output_text.insert(tk.END, "=== DAFTAR PEMESANAN ===\n")
        for pemesanan in self.sistem.pemesanan_list:
            self.output_text.insert(tk.END, pemesanan.tampilkan_info() + "\n")


def menu_utama():
    root = tk.Tk()
    app = GUISistemPemesanan(root)
    root.mainloop()


if __name__ == "__main__":
    menu_utama()
