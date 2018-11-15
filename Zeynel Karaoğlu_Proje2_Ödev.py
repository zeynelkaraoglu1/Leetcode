__author__ = " Zeynel Karaoğlu"

while True:
    print("Hava Güneşli     (1)")
    print("Hava Bulutlu     (2)")
    print("Hava Yağmurlu    (3)")
    print("Hava Karlı       (4)")
    print
    secim = input("Hava Durumunu Giriniz...:")
    isim = input ("Hangi Şehirde Yaşıyorsunuz:  ")
    if secim == "1":
        print( isim,"'da", "Bugün Hava Güneşli   ")
        print
    elif secim == "2":
        print(isim,"'da", "Bugün Hava Bulutlu   ")
    elif secim == "3":
        print(isim,"'da", "Bugün Hava Yağmurlu   ")
    elif secim == "4":
        print(isim,"'da", "Bugün Hava Karlı   ")
    else:
        pirnt ("Hava Durumu Aralığı geçersiz. Program sonlandırılıyor...")
        break