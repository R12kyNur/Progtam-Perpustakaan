from datetime import datetime, timedelta
from nama_buku import nama_buku
from nama_jurnal import nama_jurnal

def main():
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")

    tanggal_pinjam_str = input("Masukkan tanggal pinjam (DD/MM/YYYY): ")
    tanggal_pinjam = datetime.strptime(tanggal_pinjam_str, "%d/%m/%Y")

    print("\nDaftar Buku:")
    for i, buku in enumerate(nama_buku, 1):
        print(f"{i}. {buku}")

    pilihan_buku = input("Pilih maksimal 3 buku (masukkan nomor, pisahkan dengan koma, atau tekan enter untuk skip): ")
    if pilihan_buku.strip() == "":
        indeks_buku = []
    else:
        indeks_buku = [int(x.strip()) - 1 for x in pilihan_buku.split(',') if x.strip()]
        if len(indeks_buku) > 3:
            print("Maksimal 3 buku!")
            return
    buku_dipilih = [nama_buku[i] for i in indeks_buku if 0 <= i < len(nama_buku)]

    print("\nDaftar Jurnal:")
    for i, jurnal in enumerate(nama_jurnal, 1):
        print(f"{i}. {jurnal}")

    pilihan_jurnal = input("Pilih maksimal 2 jurnal (masukkan nomor, pisahkan dengan koma, atau tekan enter untuk skip): ")
    if pilihan_jurnal.strip() == "":
        indeks_jurnal = []
    else:
        indeks_jurnal = [int(x.strip()) - 1 for x in pilihan_jurnal.split(',') if x.strip()]
        if len(indeks_jurnal) > 2:
            print("Maksimal 2 jurnal!")
            return
    jurnal_dipilih = [nama_jurnal[i] for i in indeks_jurnal if 0 <= i < len(nama_jurnal)]

    tanggal_kembali = tanggal_pinjam + timedelta(days=7)

    print("\n--- Data Peminjaman ---")
    print(f"Nama: {nama}")
    print(f"NIM: {nim}")
    print(f"Tanggal Pinjam: {tanggal_pinjam.strftime('%d/%m/%Y')}")
    print(f"Tanggal Kembali: {tanggal_kembali.strftime('%d/%m/%Y')}")
    print(f"Buku Dipilih: {', '.join(buku_dipilih) if buku_dipilih else 'Tidak ada'}")
    print(f"Jurnal Dipilih: {', '.join(jurnal_dipilih) if jurnal_dipilih else 'Tidak ada'}")

if __name__ == "__main__":
    main()
