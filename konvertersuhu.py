# Konverter Suhu Lengkap (Celsius, Fahrenheit, Kelvin)

deg = "\u00B0"  # simbol derajat

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


while True:
    print("\n=== Konverter Suhu ===")
    print("1. Celsius ke Fahrenheit")
    print("2. Celsius ke Kelvin")
    print("3. Fahrenheit ke Celsius")
    print("4. Fahrenheit ke Kelvin")
    print("5. Kelvin ke Celsius")
    print("6. Kelvin ke Fahrenheit")
    print("0. Keluar")

    pilihan = input("Pilih konversi (0-6): ")

    if pilihan == "1":
        c = float(input(f"Masukkan suhu ({deg}C): "))
        print(f"{c}{deg}C = {celsius_to_fahrenheit(c):.2f}{deg}F")
    elif pilihan == "2":
        c = float(input(f"Masukkan suhu ({deg}C): "))
        print(f"{c}{deg}C = {celsius_to_kelvin(c):.2f}K")
    elif pilihan == "3":
        f = float(input(f"Masukkan suhu ({deg}F): "))
        print(f"{f}{deg}F = {fahrenheit_to_celsius(f):.2f}{deg}C")
    elif pilihan == "4":
        f = float(input(f"Masukkan suhu ({deg}F): "))
        print(f"{f}{deg}F = {fahrenheit_to_kelvin(f):.2f}K")
    elif pilihan == "5":
        k = float(input("Masukkan suhu (K): "))
        print(f"{k}K = {kelvin_to_celsius(k):.2f}{deg}C")
    elif pilihan == "6":
        k = float(input("Masukkan suhu (K): "))
        print(f"{k}K = {kelvin_to_fahrenheit(k):.2f}{deg}F")
    elif pilihan == "0":
        print("Terima kasih sudah menggunakan konverter suhu!")
        break
    else:
        print("Pilihan tidak valid!")

    # tanya apakah mau lanjut
    lanjut = input("\nMau konversi lagi? (y/n): ").lower()
    if lanjut != "y":
        print("Program selesai. Sampai jumpa!")
        break
