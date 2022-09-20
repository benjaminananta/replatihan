import os
nama_product = {
    1: 'Laptop',
    2: 'Processor',
    3: 'Mouse',
    4: 'Charger',
    5: 'Flash Disk',
}
harga_product = {
    1: '5.000.000',
    2: '3.000.000',
    3: '50.000',
    4: '100.000',
    5: '20.000',
}
data_pembeli = {}
metode_pembayaran = {
    1: 'Transfer Bank',
    2: 'Virtual Account',
    3: 'Cash on Delivery',
    4: 'Kartu Kredit',
}
os.system('cls')
print(f"================== LIST PRODUCT ==================")
for i in nama_product:
    print(f"{i}. {nama_product[i]} \tHarga : {harga_product[i]}")

konfirmasi_user = input("Apakah anda ingin Membali ? (Y/N) : ")
if konfirmasi_user == "y" or konfirmasi_user == 'Y':
    pilih_id = int(input("Pilih Nomor : "))
if pilih_id in nama_product:
    print(f"\n================== Mohon Isi Data Anda ==================")
    nama_pembeli = input("Nama : ")
    alamat = input('Alamat : ')
    no_hp = input('No_Hp / WA : ')
    kurir_pengiriman = input('Kurir Pengiriman : ')
    data_pembeli = {
        'nama_pembeli': nama_pembeli,
        'alamat': alamat,
        'no_hp': no_hp,
        'kurir_pengiriman': kurir_pengiriman,
    }
else:
    pass


if len(data_pembeli) > 0:
    print(f"\n================== Pilih Metode Pembayaran ==================")
    for i in metode_pembayaran:
        print(f"{i}. {metode_pembayaran[i]}")
    pilihan_metode_pembayaran = int(
        input("Plih Nomor Metode Pembayaran : "))
    if pilihan_metode_pembayaran in metode_pembayaran:
        print('\n================== KONFIRMASI PEMBAYARAN ANDA ==================')
        print(f"NAMA                : {data_pembeli['nama_pembeli']}")
        print(f"ALAMAT              : {data_pembeli['alamat']}")
        print(f"NO_HP / WA          : {data_pembeli['no_hp']}")
        print(f"KURIR PENGIRIMAN    : {data_pembeli['kurir_pengiriman']}")
        print(f"PRODUK              : {nama_product[pilih_id]}")
        print(f"HARGA               : {harga_product[pilih_id]}")
        print(
            f'METODE PEMBAYARAN   : {metode_pembayaran[pilihan_metode_pembayaran]}')
        konfirmasi = input(
            "Apakah Anda Yakin Ingin melakukan pembayaran ?  (Y/N) : ")
        if konfirmasi == "Y" or konfirmasi == 'y':
            print(f"\nTERIMAH KASIH PESANAN ANDA AKAN KAMI PROSES")
        else:
            pass
    else:
        pass
