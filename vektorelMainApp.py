#test app for main app
#main app is typing a wrong input

import havadurumu.havalar
import hesapmakinesi.hesaplama
import sicaklikcevirme.sicaklik
import nothesaplama.notHesap
import robotcizim.robotciz
import sayitahminoyunu.sayitahmini
import bilgiyarismasi.bilyaris
import dogumhesaplari.dogumtarihi
# import dogumhesaplari.gunlerlistesi1

def anamenu():
    print("╔" + "═"*25 +"╗")
    print("║\tGenel App\t  ║")
    print("║   1. Hava durumu\t  ║")
    print("║   2. Hesap makinesi\t  ║")
    print("║   3. Sıcaklık çevirme   ║")
    print("║   4. Not hesaplama      ║")
    print("║   5. Robot Çizimi       ║")
    print("║   6. Sayı tahmini       ║")
    print("║      Oyunu              ║")
    print("║   7. Bilgi yarışması    ║")
    print("║   8. Doğum Tarihi       ║")
    print("║      Hesapları          ║")
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
    elif secim1 == "6":
        sayitahminoyunu.sayitahmini.get_score()
        anamenu()
    elif secim1 == "7":
        bilgiyarismasi.bilyaris.byMenu()
        anamenu()
    elif secim1 == "8":
        dogumhesaplari.dogumtarihi.dtMenu()
        anamenu()
    #elif secim1 == "Q":5
    #    exit()
anamenu() # 
input()
