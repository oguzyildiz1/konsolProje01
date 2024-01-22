is_password_set = False

def get_user_data(is_password_set):
    kullanici_adi = input("Adınız? ")
    kullanici_soyadi = input("Soyadınız? ")
    kullanici_mail = input("E-mail adresiniz? ")

    # ------------ sifre oluşturma ----------------
    while True:
        if is_password_set == False:

            kullanici_password = input("\nŞifre oluşturun? ") #alttaki ile check edilecek
            kullanici_password_tekrar = input("Şifreyi tekrar giriniz ")

            if kullanici_password != kullanici_password_tekrar: #sifre tekrar ile aynı değilse
                print("Girdiğiniz şifreler eşleşmedi, tekrar deneyiniz")
            else:
                print("Şifre oluşturuldu")
                is_password_set = True
                break

            """
            else: #sifre tekrar ile aynı ise
                is_password_set = True
                break
            """

get_user_data(is_password_set)
print(is_password_set)