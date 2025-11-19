import os
os.system("cls")

print(f"{'GEROBAK FRIED CHIKEN':^30}")
print(f"{'\033[1;31mGEROBAK FRIED CHIKEN\033[0m':^42}")
print('='*30)
print(f"{"Kode":^10}{"JenisPotong":^10}{"Harga":^10}")
print('='*30)
print(f"{"D":^10}{"DADA":^10}{"Rp.2500":^10}")
print(f"{"P":^10}{"PAHA":^10}{"Rp.2000":^10}")
print(f"{"S":^10}{"SAYAP":^10}{"Rp.1500":^10}")
print('='*30)

print('silahkan pilih sesuai menu di atas')
data_belanja=[]
banyak_jenis=int(input('Masukan banyak jenis yang ingin anda beli : '))
for i in range(banyak_jenis):
    print(f'jenis ke',i+1)
    jenispotong=input('Masukan jenis potong [D/P/S] :')
    if jenispotong=='D'or jenispotong=='d':
        jenispotong="DADA"
        harga=int(2500)
    elif jenispotong=='P'or jenispotong=='p':
        jenispotong="PAHA"
        harga=int(2000)
    elif jenispotong=='S'or jenispotong=='s':
        jenispotong="SAYAP"
        harga=int(1500)
    else:
        print('kode yang anda masukan tidak ada di menu :')
        continue
    print(f"Jenis potong adalah {jenispotong}")
    print(f"harga untuk {jenispotong} adalah {harga}")
    banyakpotong=int(input('Masukan banyak potong yang ingin anda beli : '))
    jumlahharga=harga*banyakpotong
    data_belanja.append((i+1,jenispotong,harga,banyakpotong,jumlahharga))
    

print(f"{'\033[1;31mGEROBAK FRIED CHIKEN\033[0m':^60}")
print('='*54)
print(f"{"Kode":^10}{"JenisPotong":^10}{"Harga":^10} {'BanyakBeli':^10} {"JumlahHarga":^10}")
print('='*54)
jumlahbayar=0
for i in data_belanja:
    print(f"{i[0]:^10} {i[1]:^10}{i[2]:^10}{i[3]:^10}{'Rp.'}{i[4]:^10}")
    jumlahbayar+=i[4]
    pajak=jumlahbayar*0.1
    jumlahtotal=jumlahbayar+pajak
    
print('='*54)
print(f"{'Jumlah bayar Rp.':>44}  {jumlahbayar}")   
print(f"{'pajak bayar Rp.':>44}  {pajak}")   
print(f"{'TOTAL bayar Rp.':>44}  {jumlahtotal}")   
    


    
    