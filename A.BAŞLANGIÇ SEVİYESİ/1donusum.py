
#örnek 1
"""
x = input("1.sayı : ")
y = input("2.sayı : ")

toplam = int(x) + int(y)
print(toplam)
"""
#  dönüş tipi(değişken)

x = 5
y = 2.5
name = 'Çınar'
inOnline = True

x = float(x)
print(x)

# örnek 2
pi = 3.14
r = float(input("yarıçapı giriniz : "))
alan = pi * (r **2) #  ** işareti üs anlamına gelir
cevre = 2 * pi * r

print("alan : ",alan)
print("çevre : ",cevre)
# ya da 
print("alan : " + str(alan) + "  çevre : " + str(cevre))

#deneme
name = "EREN AKBAŞ"
print(name[1]) # İNDEX ile harfi gösterme

print(len(name))  # string uzunluğunu gösterir

print(name[2:4]) # 2. index ten başlayıp 4. indexe kadar gösterir.

print(name[2:9:2]) # 2. indexten 9. indexe kadar ikişer olarak gider.