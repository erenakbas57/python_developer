# fonksiyondan geriye değer değilde bir fonksiyon döndüreceğiz

def usalma(number):


    def inner(power):
        return number **power

    return inner

two = usalma(2) # taban değerine 2 gönderdik. ve two func ına atadık
print(two(4))   # üs değerine de taban two func ından alıp üsse 4 gönderdi

#------------------------------------------------------------------

def yetki_sorgula(page):
    def inner(role):
        if role == "Admin":
            return f"{role} rolünün, {page} sayfasına ulaşabilir."
        else:
            return f"{role} rolü, {page} sayfasına ulaşamaz."
    return inner

user1 = yetki_sorgula("Üye İşlemleri")
print(user1("Admin"))


#****************************************

def islem():
    def toplama():

        toplam=0
        tane = int(input("kaç değer gireceksiniz : "))
        bas = 1
        while (bas <= tane):
            sayi = int(input(f"{bas}. sayıyı gir : "))
            toplam += sayi
            bas += 1

        print(f"toplam = {toplam}")



    def carpma():
        carpim=1

        tane = int(input("kaç değer gireceksiniz : "))
        bas = 1

        while (bas<=tane):
            sayi = int(input(f"{bas}. değeri gir : "))
            carpim *=sayi
            bas+=1

        print(f"çarpma = {carpim}")


    while True:
        islem = input(f"1-toplama\n2-çarpma\n3-çıkış\n")

        if islem == "1":
            print("TOPLAMA İŞLEMİ SAYFASI AÇILIYOR")
            return toplama()
        elif islem == "2":
            print("ÇARPMA İŞLEMİ SAYFASI AÇILIYOR")
            carpma()
        elif islem == "3":
            quit()
        else:
            print("yanlış değer girdiniz .")
            continue

islem()