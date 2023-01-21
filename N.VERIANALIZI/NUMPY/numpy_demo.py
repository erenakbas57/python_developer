import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluştur
result = np.array([10,15,30,45,60])

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturun
result = np.arange(5,15,1)

# 3- (50-100) arasında beşer beşer artarak numpy dizisi oluştur
result = np.arange(50,100,5)

# 4- 10 elemanlı 0'lardan oluşan bir dizi oluştur
result = np.zeros(10)

# 5- 10 elemanlı 1'lerden oluşan dizi
result = np.ones(10)

# 6- (0-100) arası eşit aralıklı 5 sayı üret

result = np.linspace(0,100,5)

# 7- (10-30) arası rastgele 5 tane tamsayı üret
result = np.random.randint(10,30,5)

# 8- [-1 ile 1] arasında 10 adet sayı üret
result = np.random.randn(10)

# 9- (3x5) boyutunda (10-50) arası rastgele matris yap
rand = np.random.randint(10,50,15)
matrix = rand.reshape(3,5)


# 10- üretilen matrisin satır ve sütun sayıları toplamını hesapla
rowTotal = matrix.sum(axis = 1) #satır toplamı
colTotal = matrix.sum(axis = 0) #sütun toplamı
#print(f"matrix değeri :  {matrix}")
#print(f"satır toplamı : {rowTotal}")
#print(f"sütun toplamı : {colTotal}")

# 11- üretilen matrisin en büyük, en küçük ve ortalaması nedir
max = rand.max()
#print(f"max değer : {max}")
min = rand.min()
#print(f"min değer : {min}")
mean = rand.mean()
#print(f"ortalama : {mean}")

# 12- üretilen matrisin en büyük değerinin indeksi kaçtır
#result = matrix.argmax()

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz
rastgele = np.arange(10,20)
#print(rastgele)
result = rastgele[:3]

# 14- üretilen dizinin
# elemanlarını tersten yazdırın
result = rastgele[::-1]

# 15- üretilen matrisin ilk satırını seçiniz
result = matrix[0]

# 16- üretilen matrisin 2.satır ve 3.sütundaki elemanı hangisidir
result = matrix[1,2]

# 17 - üretilen matrisin tüm satırlardaki ilk elemanını seçin
result = matrix[:,0]
# üç elemanı da aldık. 0 ile ise ilk elemanlarını aldık

# 18- üretilen matrisin her bir elemanının karesini alınız
result = matrix ** 2

# 19- üretilen matris elemanlarının hangisi pozitif çift sayıdır
#     aralığı (-50 ile +50) arasında yapın
deger = np.random.randint(-50,50,15)
matris = deger.reshape(3,5)
ciftler = matris[matris % 2 == 0]
pozitifler = ciftler[ciftler >=0]


print(matris)
print(pozitifler)

