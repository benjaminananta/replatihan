import os
import locale
locale.setlocale(locale.LC_ALL, '')
tipe_menu = {
    "Sara'ba ": 6000,
    "Kopi Susu": 10000,
    "Kopi Lotong": 5000,
    "Kopi Jahe": 7000,
    "Sanggara": 15000,
}
os.system("cls")
print(f'================ DAFTAR MENU ================')
for menu in tipe_menu:
    print('\t', menu, '\t', ':', 'Rp. {0:n}'.format(tipe_menu[menu]))
print("==============================================")

menu_pilihan_user = input("Pilih Menu\t\t: ")
jumlah_pesanan = int(input("Jumlah Pesanan\t\t: "))
jumlah_bayar = jumlah_pesanan * tipe_menu[menu_pilihan_user]
print("Total Pembayaran\t: Rp. {0:n}" . format(jumlah_bayar))
print("==============================================")
pembayaran = int(input("Uang Diterima\t\t: Rp. "))
uang_kembali = pembayaran - jumlah_bayar
print("Uang Kembali\t\t: Rp. {0:n}" . format(uang_kembali))
print(f'================ SELAMAT BEKERJA ================')
