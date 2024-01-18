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


def find_zodiac(dogumAy, dogumGun):
    
    

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
    

dogumAyi = "Mart"
dogumGun = 12

find_zodiac(dogumAyi, dogumGun)
