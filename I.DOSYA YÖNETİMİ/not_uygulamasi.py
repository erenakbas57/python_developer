def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        #print(file.read())

        for satir in file:
            print(not_hesapla(satir))

def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    notlar = liste[1].split(",")
    ogrenciAdi = liste[0]

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama>=90 and ortalama<=100:
        harf = "AA"
    elif ortalama>=80 and ortalama<=89:
        harf = "BB"
    elif ortalama>=70 and ortalama<=79:
        harf = "CC"
    elif ortalama>=60 and ortalama<=69:
        harf = "DD"
    elif ortalama>=50 and ortalama<=59:
        harf = "EE"
    elif ortalama>=0 and ortalama<=49:
        harf = "FF"
    else:
        print("geçersiz değer")

    return ogrenciAdi + " : "+ harf + "\n"

def not_gir():
    ad = input("Öğrenci adı : ")
    soyad = input("Öğrenci soyadı : ")
    not1 = input("Not 1 : ")
    not2 = input("Not 2 : ")
    not3 = input("Not 3 : ")

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1+","+not2+","+ not3+ "\n")

def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sinav_sonuclari.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1- Notları oku\n2- Not gir\n3- Notları kaydet\n4- Çıkış\n")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kaydet()
    elif islem == "4":
        exit()
    else:
        print("geçersiz değer girdiniz")
        continue