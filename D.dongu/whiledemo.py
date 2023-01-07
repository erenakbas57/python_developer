sayilar = [1,3,5,7,9,12,17,21]

# sayıların elemanlarını yazdır
i=0
while (i < len(sayilar)):
    print(sayilar[i])
    i +=1
print("bitti")

# başlangıç ve bitiş değerlerini kullanıcıdan alıp sadece tek değerleri yazdırınız

bas = int(input("başlangıç değeri giriniz : "))
bit = int(input("bitiş değeri giriniz : "))
j= bas
while (j<bit):
    j += 1
    if (j%2==1):
        print(j)
print("bitti")

# kullanıcıdan belirlediği kadar sayıyı sıralama
numbers = []
i=0
adet = input("kac tane sayı gireceksiniz : ")

while i<int(adet):
    sayi = input("sayıyı giriniz : ")
    numbers.append(sayi)
    i+=1
numbers.sort()
for num in numbers:
    print(num)

# kullanıcıdan adet alıp ürün ve fiyat ekleme
urunler = []
tane = int(input("kaç adet ürün eklemek istiyorsunuz : "))
z=0
while (z<tane):
    name = input("ürün adını giriniz : ")
    price = input("ürün fiyatını giriniz : ")
    urunler.append({
        'ad': name,
        'fiyat': price
    })
    z+=1
for urun in urunler:
    print(f"ürün adı : {urun['ad']} \nfiyatı : {urun['fiyat']}")