#sayı tahmin oyunu
#1 ile 100 arasında oynanır
import random as r


def stmenu():
    print("╔" + "═"*25 +"╗")
    print("║    Sayı tahmin oyunu    ║")
    print("╠"+ "═"*25 + "╣")
    print("║    1 ila 100 arasında   ║")
    print("║    bir sayı girin:      ║")
    print("╚" + "═"*25 +"╝")

    #girdi olarak sayı alır
    girilen_sayi = 0
    score = 0 # skoru tutar
    randomNum = r.randint(1,100)#bilgisayar random olarak bir sayı belirler
    
    while randomNum != girilen_sayi: #girilen sayı ile karşılatrılır
        girilen_sayi = int(input("Sayı giriniz? "))

        if girilen_sayi < randomNum: #sayı aşağıdaysa aşağıda diye, yukarı da ise yukarıda diye söyler
            print("Sayı yukarıda")
            score += 1
        elif girilen_sayi > randomNum:
            print("Sayı aşağıda")
            score += 1
        elif girilen_sayi == randomNum:
            print(f"Tebrikler! Bilgisayar {randomNum} tutmuştu ")
            score += 1
    return score #skor burada


def get_score():
    score = stmenu()
    print(f"{score} adımda bildiniz. ")
    input()









#ve kaç tane denediğini skor olarak kaydeder


#bunu tekrar eder

