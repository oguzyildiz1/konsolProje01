##App

import hesapmakinesi.hesaplama
import havadurumu.havalar
import sicaklikcevirme.sicaklik

def anamenu():
    print("╔" + "═"*25 +"╗")
    print("║\tGenel App\t  ║")
    print("║   1. Hava durumu\t  ║")
    print("║   2. Hesap makinesi\t  ║")
    print("║   3. Sıcaklık çevirme   ║")
    print("╠"+ "═"*25 + "╣")
    print("║Seçiminiz: \t\t  ║")
    print("╚" + "═"*25 +"╝")
    secim = input()
    if secim == "1":
        hesapmakinesi.hesaplama.hmmenu()
        anamenu()
    elif secim == "2":
        havadurumu.havalar.hdmenu()
        anamenu()
    elif secim == "3":
        sicaklikcevirme.sicaklik.scmenu()
        anamenu()
    else:
        anamenu()
anamenu()
