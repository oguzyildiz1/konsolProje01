## Hesap Makinesi
def sayiSecim(): ## secim icin ayri fonksiyon kullandım
    sayi1 = int(input("1. Sayi?"))
    sayi2 = int(input("2. Sayi?"))

def hmmenu():
    print("╔" + "═" * 25 + "╗")
    print("║\tHESAP MAKİNESİ\t  ║")
    print("║\t   1. Toplama\t  ║")
    print("║\t   2. Çıkarma\t  ║")
    print("║\t   3. Çarpma\t  ║")
    print("║\t   4. Bölme\t  ║")
    print("╠" + "═" * 25 + "╣")
    print("║Seçiminiz: \t\t  ║")
    print("╚" + "═" * 25 + "╝")
    hesapSecim = input()
    if hesapSecim == "1":
        sayi1 = int(input("Sayı 1? "))
        sayi2 = int(input("Sayı 2? "))
        sonuc = sayi1 + sayi2
        print(f"Toplamları: {sonuc}\n")
    elif hesapSecim == "2":
        sayi1 = int(input("Sayı 1? "))
        sayi2 = int(input("Sayı 2? "))
        sonuc = sayi1 - sayi2
        print(f"Farkları: {sonuc}\n")
    elif hesapSecim == "3":
        sayi1 = int(input("Sayı 1? "))
        sayi2 = int(input("Sayı 2? "))
        sonuc = sayi1 * sayi2
        print(f"Çarpımları: {sonuc}\n")
    elif hesapSecim == "4":
        sayi1 = int(input("Sayı 1? "))
        sayi2 = int(input("Sayı 2? "))
        sonuc = sayi1 / sayi2
        print(f"Bölümleri: {sonuc}\n")
