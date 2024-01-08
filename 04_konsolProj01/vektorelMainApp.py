#test app for main app
#main app is typing a wrong input

import havadurumu.havalar
import hesapmakinesi.hesaplama
import sicaklikcevirme.sicaklik
import nothesaplama.notHesap
import robotcizim.robotciz

def anamenu():
    print("╔" + "═"*25 +"╗")
    print("║\tGenel App\t  ║")
    print("║   1. Hava durumu\t  ║")
    print("║   2. Hesap makinesi\t  ║")
    print("║   3. Sıcaklık çevirme   ║")
    print("║   4. Not hesaplama      ║")
    print("║   5. Robot Çizimi       ║")
    print("╠"+ "═"*25 + "╣")
    print("║Seçiminiz: \t\t  ║")
    print("╚" + "═"*25 +"╝")
    secim1 = input()
    if secim1 == "1":
        havadurumu.havalar.hdmenu()
        anamenu()
    elif secim1 == "2":
        hesapmakinesi.hesaplama.hmmenu()
        anamenu()
    elif secim1 == "3":
        sicaklikcevirme.sicaklik.scmenu()
        anamenu()
    elif secim1 == "4":
        nothesaplama.notHesap.notMenu()
        anamenu()
    elif secim1 == "5":
        robotcizim.robotciz.robciz()
        anamenu()
    #elif secim1 == "Q":5
    #    exit()
anamenu()
