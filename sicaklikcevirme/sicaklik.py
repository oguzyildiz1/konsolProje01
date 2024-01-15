#sicaklik cevirme
def scmenu():
    print("╔" + "═"*23 +"╗")
    print("║    Sıcaklık çevirme   ║")
    print("║    1. Fahrenheit      ║")
    print("║    2. Celcius         ║")
    print("╠"+ "═"*23 + "╣")
    print("║Seçiminiz: \t\t║")
    print("╚" + "═"*23 +"╝")
    secimCevirme = input()
    if secimCevirme == "1":
        #kod to fahrenheit
        celc = input("Celcius değeri? ")
        fah = int(celc) * 9 / 5 + 32
        print(f"{celc} C, {fah} fahreinheit'dır")
    elif secimCevirme == "2":
        fah = input("Fahrenheit değeri? ")
        celc = 5 / 9 * (int(fah) - 32)
        print(f"{fah} F, {celc} celcius'dur")
        #kod to celcius
    input()
