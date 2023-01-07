sayilar = [6,12,34,21,56,11,9,17,22]
sayilar.sort()

# üçe bölünen sayıları yazdır

for sayi in sayilar:
    if (sayi%3==0):
        print(sayi)

# sayıların toplamını yazdır

toplam=0
for sayi1 in sayilar:
    toplam +=sayi1
print(toplam)

#****************************************

sehirler = ['istanbul','rize','izmir','ankara','kastamonu','kars','sinop']
sehirler.sort()

# en fazla beş harfli şehirleri yazdırınız

for sehir in sehirler:
    if (len(sehir)<=5):
        print(sehir)

#****************************************

telefon = [
    {'model':'samsung s6','price':'3000'},
    {'model':'samsung s7','price':'4000'},
    {'model':'samsung s8','price':'5000'},
    {'model':'samsung s9','price':'6000'},
    {'model':'samsung s10','price':'7000'}
]

# telefonların fiyatları toplamı nedir
toplamtel=0

for tel in telefon:
    fiyat = int(tel['price'])
    toplamtel += fiyat
print(toplamtel)

# telefonlardan en fazla 5000 olanları görüntüle

for phone in telefon:
    if (int(phone['price'])<=5000):
        print(phone['model'])   