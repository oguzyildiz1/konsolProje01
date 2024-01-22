import time


def are_inputs_true(ad="default", soyadi="default", email="default@gmail.com"):
    user_data = [] # kullanıcı verilerini tutan liste
    number_list = ["1","2","3","4","5","6","7","8","9","0"]
    print(user_data)
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

    print(email)
    if "@" not in email or "." not in email:
        yanlis = "e: email"
        return yanlis
    else:
        email_cleaned = email.strip()
        user_data.append(email_cleaned)

    return user_data
    


kullanici_adi = "oguzhan"
kullanici_soyadi = "yil1diz"
kullanici_mail ="asdf@gmail.com"

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
        print(check_user_data)
        break