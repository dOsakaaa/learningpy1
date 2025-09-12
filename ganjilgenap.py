while True:
    angka = int(input("Masukkan angka: "))
    
    if angka % 2 == 0:
       
       print("Angka ini Genap")
    else : 
       print("Angka ini Ganjil")

    ulang = input("Mau cek nilai lagi? (y/n) "). lower()
    if ulang != "y":
        print("Program selesai, Terima Kasih")
        break
