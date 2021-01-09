from datetime import *
import os

if(os.path.exists("dataPinjaman.txt")) :
    fileMode = 'a'
else :
    fileMode = 'w'

file = open("dataPinjaman.txt", fileMode)
while True :   
    kode = input("Masukkan Kode Member : ")
    nama = input("Masukkan Nama Member : ")
    judul = input("Masukkan Judul Buku : ")

    TglPinjam = date.today()
    TglKembali = TglPinjam + timedelta(days = 7)

    dataPinjaman = [kode, nama, judul, str(TglPinjam), str(TglKembali) + '\n']
    file.write('|'.join(dataPinjaman))
    konfirmasi = input("\nUlangi lagi (Y/N) : ")
    if(konfirmasi.lower() == 'y') or (konfirmasi.lower() == 'Y') :
        continue  
    elif(konfirmasi.lower() == 'n') or (konfirmasi.lower() == 'N') :
        break
    else :
        print("Input tidak valid")
        break
file.close()
