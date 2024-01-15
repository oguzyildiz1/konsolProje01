# bilgi yarışması programı
import random
import time

# --------------  --------
#def puanTablosu():

# tanitim
def byMenu(): # bilgi yarışması ana menu
    print("╔" + "═"*30 +"╗")
    print("║        Bilgi Yarışması       ║")
    print("╠"+ "═"*30 + "╣")
    print("║  Genel kültür ile alakalı    ║")
    print("║    5 soru sorulacaktır.      ║")
    print("║                              ║")
    print("║  Cevapları küçük harf ile    ║")
    print("║    giriniz.                  ║")
    print("╠"+ "═"*30 + "╣")
    print("║ Başlamak için: 1'i tuşlayın  ║")
    print("╚" + "═"*30 +"╝")

    input()

    while True:
        print("\nYarışma Başlıyor...",end="")
        time.sleep(1.6)
        print(" Bol şans!") 
        time.sleep(0.4)
        soruSecimListesi = soruSec()
        soruSor(soruSecimListesi)
        tekrar = input("\nTekrar oynamak istermisin? (e / h) ") 

        if tekrar == "h":
            break

#input("\nBir renk secin? ")

# --------------------  Alakasız


#soru sorma oyunu

# 1. Hangisi periyodik tabloda bulunan bir element değildir? Azot Oksijen Su
# 2. Hangisi bir doğal sayıdır? 2.4 -2 0
# 3. Hangisi tarihteki Türk devletlerinden biri değildir? Avar Kağanlığı, Emevi devleti Hun imparatorluğu,
# 4. Galatasaray hangi yıl UEFA kupasını kazanmıştır? 2000, 2001, 2002
# 5. Hangi hayvan memeli değildir? Penguen, yarasa, yunus
# 6. Osmanlı İmparatorluğu yaklaşık kac asır hüküm sürmüştür? 5 6 7
# 7. 1 metre kaç milimetredir? 100 1000 100000
# 8. Hangi ülke Asya kıtasındadır? Peru Madagaskar Singapur
# 9. Cristiano Ronaldo daha önce hangi futbol takımında oynamıştır? Liverpool Bayern Munich Manchester United
# 10. Hangisi kuvvet birimidir? Newton Pascal Kilogram
# 11. Fatih Sultan Mehmet’in babası kimdir? I. Mehmet Yıldırım Beyazıt II. Murat
# 12. Mısır'ın başkenti neresidir? Kahire Kazablanka Cakarta

sorular = {
    "1" : "Hangisi periyodik tabloda bulunan bir element değildir?",
    "2" : "Hangisi bir doğal sayıdır?",
    "3" : "Hangisi tarihteki Türk devletlerinden biri değildir?",
    "4" : "Galatasaray hangi yıl UEFA kupasını kazanmıştır?",
    "5" : "Hangi hayvan memeli değildir?",
    "6" : "Osmanlı İmparatorluğu yaklaşık kac asır hüküm sürmüştür?",
    "7" : "1 metre kaç milimetredir?",
    "8" : "Hangi ülke Asya kıtasındadır?",
    "9" : "Cristiano Ronaldo daha önce hangi futbol takımında oynamıştır?",
    "10": "Hangisi kuvvet birimidir?",
    # "11": "Fatih Sultan Mehmet’in babası kimdir?",
    # "12": "Mısır'ın başkenti hangi şehirdir?"
    }

cevaplar = {
    "1" : ["a)Azot  b)Oksijen  c)Su","c"], # doğru cevap 1. indekste sonda
    "2" : ["a)2.4    b)-2    c)0","c"],
    "3" : ["a)Avar Kağanlığı    b)Emevi devleti   c) Hun imparatorluğu","b"],
    "4" : ["a)2000   b)2001   c)2002","a"],
    "5" : ["a)penguen    b)yarasa    c)yunus","a"],
    "6" : ["a)5    b)6    c)7","b"],
    "7" : ["a)100    b)1000    c)10000","b"],
    "8" : ["a)Peru    b)Madagaskar    c)Singapur","c"],
    "9" : ["a)Liverpool    b)Bayern Munich    c)Manchester United","c"],
    "10": ["a)Newton    b)Pascal    c)Kilogram","a"]
    }


def soruSor(soruSecimListesi):
    soruSirasi = 1
    skor = 0 # skor
    #soru sorma:
    for j in soruSecimListesi:
        time.sleep(1) # 1 saniye bekliyor sorular arasında
        j = str(j) #soru numarasını str değere çeviriyor.
    #print(j, "type: ", type(j))
        print(f"\n{soruSirasi}.", sorular[j])
        testSecim = input(f"{cevaplar[j][0]}\n") # cevaplar kümesinden 0. indeks

        time.sleep(1)

        if testSecim == cevaplar[j][1]: # doğru cevaplar bu indekste 
            print(f"Doğru cevap. ")
            skor += 1 # skor tutuyoruz
        else:
            print(f"Yanlış cevap. Doğru {cevaplar[j][1]} şıkkı olacaktı.")

        soruSirasi += 1
    
    print("\nSonuc: ",end="")
    time.sleep(2)
    print(f"{skor} doğru yaptınız.\n")
    time.sleep(1)
    print("Puanınız:", (skor * 100) / soruSayisi, "/ 100") # skor
    time.sleep(1)

def soruSec(): # soru secim listesine 5 tane raslantısal soru seçiyor.
    i = 1 #
    soruSecimListesi = []    
    
    global soruSayisi
    soruSayisi = 5 # soru sayisi

    while i <= soruSayisi: #soru sayısı beş tane olacak
        ranA = random.randint(1,10) # cekilen soru numarası

        if ranA in soruSecimListesi: # eğer soru listede ise aynı soruyu eklemiyor
            continue

        soruSecimListesi.append(ranA) # liste
        i += 1

    return soruSecimListesi

#soruSecimListesi = [] # secilen soru sıralması
 # 1. 2. .3 diye secilen listesindeki soruları soruyor. 

#soruSecimListesi = soruSec()

#soruSor(soruSecimListesi)

input()

