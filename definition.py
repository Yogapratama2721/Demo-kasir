import os
import time
os.system("cls")
def kasirwhile ():
    print('='*35)
    print(f"selamat berbelanja di toko amanah".title())
    print('='*35)
    keranjang=[
        
    ]
    print(f"1.shampo\t2.handuk\n3.sabun\t\t4.susu\n5.mie\t\t6.sayuran\nSilahkan pilih menggunakan nama dari barang di atas : ".title())
    while True:
        try:
            barang=input(str("\nsilahkan masukan pilihanmu atau ketik 'selesai' untuk mengakhiri belanja : ")).upper()
            if barang=="SUSU":
               nama="susu"
               harga=2500
            elif barang=="SABUN":
                nama="sabun"
                harga=5000
            elif barang=="SHAMPO":
                nama="shampo"
                harga=2500
            elif barang=="HANDUK":
                nama="handuk"
                harga=15000
            elif barang=="SHAMPO":
                nama="shampo"
                harga=2500
            elif barang=="MIE":
                nama="mie"
                harga=3500
            elif barang=="SAYURAN":
                nama="sayuran"
                harga=3500
            elif barang=="SELESAI":
               
                break
            else:
                print("nama barang yang anda masukan tidak ada pada daftar!!!".upper())
                continue       
        except:
            print("kesalahan menginput data\nGunakan nama barang untuk menambahke keranjang")
            continue
        try:
            jumlah=int(input("masukan jumlah barang : "))
            print(f"{jumlah} {nama} dengan harga satuan Rp{harga},\nTelah di tambahkan ke dalam keranjang!!".title())
            hargatotal=harga*jumlah
            keranjang.append(('-',nama,jumlah,hargatotal))
        except:
            print("masukan angka untuk menambahkan jumlah ".upper())
            continue
    print("="*42)
    print(f"{"Daftar Barang Belanja Anda":^42}")
    print("="*42)
    totalbelanja=0
    print("NO\tNAMABARANG\tJUMLAH\tHARGATOTAL")
    print("="*42)
    for i in keranjang:
        print(f"{i[0]}\t{i[1]}\t\t{i[2]}\t{"Rp."}{i[3]}")
        totalbelanja+=i[3]
    print(f"\nharga yang harus anda bayar \tRp.{totalbelanja}\n")
    keranjang.sort(key=lambda y:len(y))
    # print(f"sortir barang belanja menggunakan len {keranjang}")
    konfirmasi=input("silahkan cek kembali barang belanjaan anda\napakah belanja anda sudah benar? [y/n] ").upper()
    if konfirmasi=='Y':
        while True:
            try:
                bayar=int(input(f"\nsilahkan masukan jumlah uang anda untuk membayar : "))
                if bayar>=totalbelanja:
                    kembalian=bayar-totalbelanja
                    print(f"{"Pembayaranmu sedang di proses....":^42}\n")
                    time.sleep(1)
                    print(f"{"Pembayaran Berhasil !!!!":^42}")
                    print("="*42)
                    print(f"uang  anda diterima senilai Rp.{bayar}\nuang kembalian anda selnilai  Rp.{kembalian}")
                    print("="*42)
                    print(f"terimakasih sudah berbelanja di toko kami".upper())
                    print("="*42)
                    break
                else:
                    print(f"{"Pembayaranmu sedang di proses....":^42}\n")
                    time.sleep(1)
                    print(f"{"Pembayaran GAGAL!!":^42}\n")
                    print("uang anda tidak cukup untuk membayar total belanja anda!!")
                    continue
            except:
                print("masukan angka nominal not str!!!")
                continue
    else:
        print(f"silahkan ulangi pengisian keranjang".upper()) 
        kasirwhile()
kasirwhile()