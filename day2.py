first_name ="labarka"
food = "spagedi"
person = "trippi troppi"

# Sigma banget jir

# Gila gila ekh


    # Aduh kebelet eek

def konversi_wl(wl):
    # Hitung DL dan BGL
    dl = wl // 100
    sisa_wl = wl % 100

    bgl = dl // 100
    sisa_dl = dl % 100

    return bgl, sisa_dl, sisa_wl

def main():
    print("=== Konversi WL ke DL & BGL ===")
    while True:
        try:
            wl = int(input("\nMasukkan jumlah World Lock (WL): "))
            bgl, dl, sisa_wl = konversi_wl(wl)

            print(f"\nHasil konversi:")
            print(f"{wl} WL = {bgl} BGL, {dl} DL, {sisa_wl} WL")

        except ValueError:
            print("⚠️ Masukkan angka yang valid!")
            continue

        # Tanya apakah mau lanjut
        lagi = input("\nMau konversi lagi? (y/n): ").lower()
        if lagi != "y":
            print("Terima kasih sudah pakai konverter ini!")
            break

if __name__ == "__main__":
    main()
