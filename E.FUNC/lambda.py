#map() Fonksiyonu:
#Parametre olarak aldığı fonksiyona,
#parametre olarak aldığı listenin her elemanını sırasıyla parametre olarak gönderir.

#normal func kullanımı
def karealma(sayi): return sayi**2
kare = lambda num:num**2

print(kare(3))

myList = [1,2,3,4,5,6,7,8,9]

result3 = list(map(kare,myList))

result =list(map(karealma,myList))

#lambda kullanımı
result2 = list(map(lambda number: number**2,myList))
print(result)
print(result2)
print(result3)

#*********************************************************

myList2 = [1,2,3,4,5,6,7,8,9,0]
#Filter bir fonksiyondan True dönen elementler için bir liste oluşturur.

check_even = lambda num:num%2==0

deger = list(filter(check_even,myList2))
print(deger)