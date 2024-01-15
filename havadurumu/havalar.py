## Hava durumu programı
def hdmenu():
    print("╔" + "═"*25 +"╗")
    print("║\tHava Durumu\t  ║")
    print("║   1. Gündüz\t\t  ║")
    print("║   2. Gece\t\t  ║")
    print("╠"+ "═"*25 + "╣")
    print("║Seçiminiz: \t\t  ║")
    print("╚" + "═"*25 +"╝")
    secimHava = input()
    if secimHava == "1": #gündüz seçimi
        sicakGunduz = 13
        print(f"Sıcaklık gündüz {sicakGunduz} derece.\n")
    elif secimHava == "2":
        sicakGece = 3
        print(f"Sıcaklık bu gece {sicakGece} derece olacak.\n")