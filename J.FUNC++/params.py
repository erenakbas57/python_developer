# parametre olarak fonksiyon gönderme

def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b


def islem(f1,f2,f3,f4):
    while True:
        islem_adi = input(f"1-toplama ** 2-çıkarma ** 3-çarpma ** 4-bölme ** 5-çıkış\nHangi işlemi yapmak istiyorsanız sayısını giriniz : ")

        if islem_adi == "1":
            deger1 = int(input("1.sayı : "))
            deger2 = int(input("2.sayı : "))
            sonuc = f1(deger1,deger2)
            print(f"{deger1} + {deger2} = {sonuc}")
        elif islem_adi == "2":
            deger1 = int(input("1.sayı : "))
            deger2 = int(input("2.sayı : "))
            sonuc = f2(deger1, deger2)
            print(f"{deger1} - {deger2} = {sonuc}")
        elif islem_adi == "3":
            deger1 = int(input("1.sayı : "))
            deger2 = int(input("2.sayı : "))
            sonuc = f3(deger1, deger2)
            print(f"{deger1} * {deger2} = {sonuc}")
        elif islem_adi == "4":
            deger1 = int(input("1.sayı : "))
            deger2 = int(input("2.sayı : "))
            sonuc = f4(deger1, deger2)
            print(f"{deger1} / {deger2} = {sonuc}")
        elif islem_adi == "5":
            break
        else:
            print("geçersiz değer girdiniz")


islem(toplama,cikarma,carpma,bolme)