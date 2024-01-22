#kayıt olma programı
import time


yanlis = "" #kullanıcı yanlış girdi girerse bu var değişecek
is_password_set = False


def komenu():
    print("╔" + "═" * 28 + "╗")
    print("║          KAYIT OL          ║")
    print("║  1. Kullanıcı bilgilerini  ║")
    print("║     giriniz                ║")
    print("║  2. Kullanıcı bilgilerini  ║")
    print("║     yazdırın               ║")
    print("╠" + "═" * 28 + "╣")
    print("║Seçiminiz:                  ║")
    print("╚" + "═" * 28 + "╝")

    secim = input()
    
    if secim == "1":
        #kullanıcı bilgilerini al
        get_user_data(is_password_set)
#email, ad, soyad, not ve password

#kullanıcı bilgilerini al


def get_user_data(is_password_set):
    kullanici_adi = input("Adınız? ")
    kullanici_soyadi = input("Soyadınız? ")
    kullanici_mail = input("E-mail adresiniz? ")

    # ------------ sifre oluşturma ----------------
    while is_password_set == False:
        kullanici_password = input("\nŞifre oluşturun? ") #alttaki ile check edilecek
        kullanici_password_tekrar = input("Şifreyi tekrar giriniz ")

        if kullanici_password != kullanici_password_tekrar: #sifre tekrar ile aynı değilse
            print("Girdiğiniz şifreler eşleşmedi, tekrar deneyiniz")
        else:
            print("Şifre oluşturuldu")
            is_password_set = True
    # ------------ sifre oluşturma bitti ---------------
            
    #--------- girdi yanlışlarını belirleme ----------
                
    while True:
        check_user_data = are_inputs_true(kullanici_adi, kullanici_soyadi, kullanici_mail)
        
        if type(check_user_data) == str:
            match check_user_data: #gelen verileri kontrol ediyor.
                case "e: ad":
                    print("Yanlış ad girildi. Tekrar deneyiniz.")
                    kullanici_adi = input("Adınız? ")
                    # kullanici_adi = input("Adınız? ")
                    # are_inputs_true(ad=kullanici_adi)
                case "e: soyadi":
                    print("Yanlış soyadı girildi. Tekrar deneyiniz. ")
                    kullanici_soyadi = input("Soyadınız? ")
                    # kullanici_soyadi = input("Soyadınız? ")
                    # are_inputs_true(soyadi=kullanici_soyadi)
                case "e: email":
                    print("Yanlış e-mail girildi. Tekrar giriniz. ")
                    kullanici_mail = input("Email adresinis? ")
                    # kullanici_mail = input("E-mail adresiniz? ")
                    # are_inputs_true(email = kullanici_mail)
                case _:
                    time.sleep(0.5)
                    print("\nKaydınız başarıyla oluşturuldu!")
                    break

        elif type(check_user_data) == list:
            user_data = check_user_data # -----  user data burada kayıt oluyor.!!!!
            user_data.append(kullanici_password)
            print(user_data)
            time.sleep(0.5)
            print("\nKaydınız başarıyla oluşturuldu!")

            return user_data
    # ---- kullanıcı verileri toplandı -------

#girilen veriler doğru mu test et
def are_inputs_true(ad="default", soyadi="default", email="default@gmail.com"):
    user_data = [] # kullanıcı verilerini tutan liste
    number_list = ["1","2","3","4","5","6","7","8","9","0"]
    #adın içinde numara var mı bakacaz...
    for i in ad:
        if i in number_list:
            yanlis = "e: ad" #yanlış olarak numara girildi.
            return yanlis
    
    ad_cleaned = ad.strip()
    user_data.append(ad_cleaned) #listeye gelen veriyi temizlenmiş olarak ekliyor...

    for j in soyadi:
        if j in number_list:
            yanlis = "e: soyadi" #yanlış olarak numara girildi.
            return yanlis
    
    soyadi_cleaned = soyadi.strip()
    user_data.append(soyadi_cleaned)

    if "@" not in email or "." not in email:
        yanlis = "e: email"
        return yanlis
    else:
        email_cleaned = email.strip()
        user_data.append(email_cleaned)

    return user_data

#kullanıcı bilgilerini kaydet
#code....


#takvim ile bir görev sistemi oluştur
    
#bir not al..datetime() kullan


#isteyince bas
