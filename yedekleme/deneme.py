def setDaysTurkish():
    gunler = {"Monday" : "Pazartesi","Tuesday" : "Salı","Wednesday" : "Çarşamba",
              "Thursday" : "Perşembe","Friday" : "Cuma","Saturday" : "Cumartesi",
              "Sunday" : "Pazar"}
    
    return gunler


def setMonthsTurkish():
    aylar = {"January" : "Ocak","February" : "Şubat", "March" : "Mart",
              "April" : "Nisan", "May" : "Mayıs", "June" : "Haziran",
              "July" : "Temmuz", "August" : "Ağustos", "September" : "Eylül",
              "October" : "Ekim", "November" : "Kasım", "December" : "Aralık"
              }
    
    return aylar

"""
def setZodiacSign():
    signs = {
        "Koç" : ["21 Mart", "20 Nisan"],
        "Boğa" : ["21 Nisan", "20 Mayıs"],
        "İkizler" : ["21 Mayıs", "21 Haziran"],
        "Yengeç" : ["22 Haziran", "22 Temmuz"],
        "Aslan" : ["23 Temmuz", "22 Ağustos"],
        "Başak" : ["23 Ağustos", "22 Eylül"],
        "Terazi" : ["23 Eylül", "23 Ekim"],
        "Akrep" : ["24 Ekim", "22 Kasım"],
        "Yay" : ["23 Kasım", "21 Aralık"],
        "Oğlak" : ["22 Aralık", "20 Ocak"],
        "Kova" : ["21 Ocak", "18 Şubat"],
        "Balık" : ["19 Şubat", "20 Mart"],
            }
    
    return signs
"""
def set_zodiac_sign_3(): # son liste(çalışıyor)
    signs = [
        {"Koc" : ("Mart", 21)}, {"Boğa" : ("Nisan", 21)}, {"İkizler" : ("Mayıs", 21)},
        {"Yengeç" : ("Haziran", 22)}, {"Aslan" : ("Temmuz", 23)}, {"Başak" : ("Ağustos", 23)},
        {"Terazi" : ("Eylül", 23)}, {"Akrep" : ("Ekim", 24)}, {"Yay" : ("Kasım", 23)}, 
        {"Oğlak" : ("Aralık", 22)}, {"Kova" : ("Ocak", 21)}, {"Balık" : ("Şubat", 19)}
    ]
    
    return signs

"""
#---------------- bu dictionary liste içersinde yazılacak
def set_zodiac_sign_2(): 
    signs = {
        "Koç" : "21 Mart",
        "Boğa" : "21 Nisan",
        "İkizler" : "21 Mayıs",
        "Yengeç" : "22 Haziran",
        "Aslan" : "23 Temmuz",
        "Başak" : "23 Ağustos",
        "Terazi" : "23 Eylül",
        "Akrep" : "24 Ekim",
        "Yay" : "23 Kasım",
        "Oğlak" : "22 Aralık",
        "Kova" : "21 Ocak",
        "Balık" : "19 Şubat",
            }
    
    return signs
"""

# --------------- burada kaldım ---------------
def find_zodiac(dogumAy, dogumGun):
    signs = set_zodiac_sign_3() # burc listesini alıyor

    #dogumAy, dogumGun #girilen doğum ayı, ve günü
    #onceki_ay = ""
    print(signs[3]) # {'Koc': ('Mart', 21)}
    key = 0
    
    for i in signs:
        #print(signs[key] ," sırası")
        # index numarasını tutyor
        # print(i.keys()) # dict_keys(['İkizler'])
        # print(i) # dizideki değişkenleri veriyor {'Koc': ('Mart', 21)}
        for j in i:
            """
            print(" ", j, end=", ") #koc
            print(" ", i[j], end=", ") #('Mart', 21)
            print(" ", i[j][0]) # Mart 
            print(" ", i[j][1]) # 21 
            """
            if i[j][0] == dogumAy: # girilen ay bu tupledaki ay ise
                if dogumGun >= i[j][1]: # ve girilen gün burcun başlangıç gününden fazlaysa
                    print("Burcunuz:", j) # burcunuzu bulduk
                    break
                elif dogumGun < i[j][1]:
                    for a in signs[key-1]: # burucunu veriyor
                        print("Burcunuz:", a)
                    #print("c:", dogumGun, i[j][0]) # 18 Nisan
                    #print("Burcunuz:", signs[key-1][j][0], "key :", key-1, )
                    #print(signs[key-1][j])
                    break
        key += 1 # index numarasını tutuyor.
             
'''
    for i in signs:
        splitted_data = signs[i].split() #['21','Mart']
        burc_baslangic_gunleri = int(splitted_data[0]) #['21']
        burc_aylari = splitted_data[1] #['Mart'] #hazır burç listesindeki data
        #Girdiğimiz aya göre o ayın burcunu yazacak.
        print(dogumAy)
        if dogumAy == "Mart": #mart'a özel bir durum
            if dogumGun < burc_baslangic_gunleri:
                print("Burcunuz: Balık burcu")
            elif dogumGun >= burc_baslangic_gunleri:
                print(f"Burcunuz: {i}")
        elif dogumAy == burc_aylari: # girilen ay ise nisan
            if dogumGun < burc_baslangic_gunleri:
                print(f"Burcunuz: ")
            if dogumGun >= burc_baslangic_gunleri:
                print(f"Burcunuz: {i}")


        #print(splitted_data)
'''
    
"""
def findZodiacSign(dogumA, dogumG):
    signs = setZodiacSign()
    #print(dogumA, dogumG)

    ## doğum ayını belirle
    
    #---------------- --------------------------
    
    for i in signs: # burç listesinde döngü
        #print(i,signs[i])
        
        if True:
            test = signs[i][0] #Burcun başlangıç ve bitiş zamanı,
            #bize ne lazım? Ay ve gün
            # parçalama yapalım
            splitted_text = test.split() # gün ve ay olarak ayırır
            ay_splitted = splitted_text[1]
            gun_splitted = int(splitted_text[0])
            
            print(ay_splitted, " splitted") # ay belirlendi
            
            if dogumA == ay_splitted:
                print(f"{ay_splitted}'da doğmuşsun")
                
                if dogumG >= gun_splitted:
                    print(f"{gun_splitted}' günü doğmuşsun")
                    print(f"{i} burcusun")
                
                break
        
    print(signs["Koç"][0])
    
"""

dogumAyi = "Mart"
dogumGun = 15

find_zodiac(dogumAyi, dogumGun)
