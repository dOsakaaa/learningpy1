while True:
    nilai = int(input("Masukkan nilai ujian kamu: "))

    if nilai >= 90:
        print("Nilai A - Sangat Baik! 🎉")
    elif nilai >= 80:
        print("Nilai B - Baik 👍")
    elif nilai >= 70:
        print("Nilai C - Cukup 🙂")
    elif nilai >= 60:
        print("Nilai D - Hampir lulus 😅")
    else:
        print("Nilai E - Tidak lulus, semangat ya 💪")

    # tanya apakah mau ulang lagi
    ulang = input("Mau cek nilai lagi? (y/n): ").lower()
    if ulang != "y":
        print("Program selesai, terima kasih 😊")
        break
