#dogum günleri programları
import datetime
import dogumhesaplari.gunlerlistesi1 #klasör isimini de girmek gerekiyor. /E


dogumTar = ""
isTarihSet = False
# gelen tarihi yıl, ay ve gün olarak ayırır ve int olarak listeye ekler
def tarihAyirma(para1):
    tarih = para1
    y = 0
    dogumZamanList = [] # doğum değerlerinin tutulacağı liste
    
    for i in range(len(tarih)):
        #print(i, tarih[i])
        if tarih[i] == " " : #boşluğa göre tarihi parçalıyor.
            #print(tarih[y:i]) # ilk boşluktan önceki sayılar 
            dogumZamanList.append(int(tarih[y:i])) # listedeki ilk değer ay, sonraki, gün
            y = i + 1 # y indeks değerinde ilk boşluk var.
        elif i == len(tarih) -1 :
            #print(tarih[y:i+1]) #
            dogumZamanList.append(int(tarih[y:i+1])) # listedek son değer yıl
    
    return dogumZamanList
#def yasBulma():
            
def dtMenu():
    print("╔" + "═"*25 +"╗")
    print("║     Doğum Bilgileri     ║")
    print("║   1. Kaç yaşındasınız?  ║")
    print("║   2. Doğduğunuz gün     ║")
    print("║   3. Burcunuz           ║")
    print("║   4. Yeni tarih giriniz ║")
    print("║   5. Çıkış              ║")
    print("╚" + "═"*25 +"╝")
    tarihAyarlama()
    
    
def tarihAyarlama(): #tarihi ayarlama fonksiyonu
    global isTarihSet
    
    while isTarihSet == False: # tarih belirlenince while'dan çıkıyor.
        global dogumTar
        dogumTar = input("Doğum yılınız (Ay gün yıl)? ") # doğumtarihi girişi 
        
        if dogumTar.find(" ") == -1: # tarih düzgün girişmediyse
            print("Lütfen yılınız boşluk bırakarak giriniz.\n")
        else:
            isTarihSet = True
    
    dogumZamanList = tarihAyirma(dogumTar) #girilen tarihi ayarlıyor
    dogumBil = datetime.datetime(dogumZamanList[-1],dogumZamanList[0],dogumZamanList[1])
    simdikiZaman = datetime.datetime.now() # simdiki tarih
    
    secimIslemleri(dogumBil, simdikiZaman)
     # Tarih girildi...


def secimIslemleri(dogumBil, simdikiZaman):
    secim = input("Seçiminiz: ")

    if secim == "1":
        print("\nYaşınız: ",int(simdikiZaman.strftime("%Y")) - int(dogumBil.strftime("%Y")))
        input()
        dtMenu()
    if secim == "2":
        gunlerTurkce = dogumhesaplari.gunlerlistesi1.setDaysTurkish() #günler listesi burada tutuluyor (turkce / ingilizce)
        #klasör ismini de girmek gerekiyor....
        dogumGunu = dogumBil.strftime("%A")
        print(dogumBil.strftime("%Y"),"yılında doğduğunuz gün:", gunlerTurkce[dogumGunu])
        #print(gunlerTurkce["Monday"])
        input()
        dtMenu()

        
    


# dtMenu()