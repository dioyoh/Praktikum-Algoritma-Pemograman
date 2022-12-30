# Halaman 57 Modul Praktikum Algoritma Pemrograman
# Create by Dio Yohannes Simbolon-2270231015


print("Selamat Datang di Warung Sate MADURA Cak Abas")
nama = input("Masukan Nama Anda: ")
tanggal = input("Tanggal Pembelian: ")
alamat = input("Masukan Alamat Anda: ")
telpon = input("Masuk No.Telp Anda: ")

def fungsilist():
    global totalbeli
    global jumlah
    global ltr
    print ("\n-----List Bahan Bakar-----\n")
    print("1. Sate Ayam = Rp 28.000/Porsi")
    print("2. Sate Kambing = Rp 40.000/Porsi")
    print("3. Sop Kambing = Rp 32.000/Porsi")
    nomor=int(input("Masukan Pilihan: "))
    jumlah=int(input("Berapa Porsi: "))
    
    if nomor==1:
       totalbeli=jumlah*28.000
       print (jumlah," Perporsi Ayam = Rp", totalbeli)
       ltr=("Perposi Ayam")
    elif nomor==2:
       totalbeli=jumlah*40.000
       print (jumlah," Perporsi Kambing = Rp", totalbeli)
       ltr=("Perposrsi Kambing")
    elif nomor==3:
       totalbeli=jumlah*32.000
       print (jumlah, " Perporsi Sop Kambing = Rp", totalbeli)
       ltr=("Perporsi Sop Kambing")
    else:
      print("Pilihan tidak ada, silahkan masukan lagi!!!")
fungsilist()

print("\nTotal harus Dibayar: Rp",totalbeli)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalbeli)
print("Kembalian :",kembalian)

print("==========Bon Pembayaran==========")
print ("Nama\t\t\t\t:",nama)
print ("Alamat\t\t\t\t:",alamat)
print ("Tanggal Pembelian\t\t:",tanggal)
print ("No.Telp\t\t\t\t:",telpon)
print ("Beli\t\t\t\t:",jumlah,ltr,"( Rp", totalbeli,")")
print ("Tagihan\t\t\t\t: Rp",totalbeli)
print ("Dibayar\t\t\t\t: Rp",uang)
print ("Kembalian\t\t\t: Rp",kembalian)
print("==========Terima Kasih=========")