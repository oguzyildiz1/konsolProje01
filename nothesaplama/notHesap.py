#dönem sonu notunu hespalar
#girilen ilk sınav ikinci sınav ve final notları ile kaç puan aldığınızı basar.
def notMenu():
    print("╔" + "═"*30 +"╗")
    print("║        Not hesaplama         ║")
    print("║    1. Sınav notunu girin     ║")
    print("║    2. Sınav notunu girin     ║")
    print("║      Final notunu girin      ║")
    print("╠"+ "═"*30 + "╣")
    print("║ Notları 100 üzerinden girin  ║")
    print("╚" + "═"*30 +"╝")
    #not girişleri 
    not1 = int(input("1. Sınav notu? "))
    not2 = int(input("2. Sınav notu? "))
    final = int(input("Final notu? "))
    # son notu hesaplama
    if not1 < 0 or not1 > 100:
        print("Yanlış not girdiniz")
    elif not2 < 0 or not2 > 100:
        print("Yanlış not girdiniz")
    elif final < 0 or final > 100:
        print("Yanlış not girdiniz")
    else:
        #not dağılımı 30%, 30% ,40%
        sonNot = not1 * 0.3 + not2 * 0.3 + final * 0.4
        if sonNot >= 90:
            print(f"Yıl sonu notunuz {sonNot}! 'A' aldınız. Mükemmel, tebrikler!")
        elif sonNot >= 80:
            print(f"Yıl sonu notunuz {sonNot}! 'B' aldınız. Çok iyi, tebrikler!")
        elif sonNot >= 70:
            print(f"Yıl sonu notunuz {sonNot}! 'C' aldınız. Geçtiniz, tebrikler!")
        else:
            print(f"Yıl sonu notunuz {sonNot}! 'F' aldınız. Kaldınız!")
        input()