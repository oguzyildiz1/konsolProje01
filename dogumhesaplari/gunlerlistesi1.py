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


def set_zodiac_sign(): # son liste(çalışıyor)
    signs = [
        {"Koc" : ("Mart", 21)}, {"Boğa" : ("Nisan", 21)}, {"İkizler" : ("Mayıs", 21)},
        {"Yengeç" : ("Haziran", 22)}, {"Aslan" : ("Temmuz", 23)}, {"Başak" : ("Ağustos", 23)},
        {"Terazi" : ("Eylül", 23)}, {"Akrep" : ("Ekim", 24)}, {"Yay" : ("Kasım", 23)}, 
        {"Oğlak" : ("Aralık", 22)}, {"Kova" : ("Ocak", 21)}, {"Balık" : ("Şubat", 19)}
    ]
    
    return signs