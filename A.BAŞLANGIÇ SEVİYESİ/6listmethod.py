numbers = [12,54,85,75,63,52,1,25,96,85,32,20,41]
letters = ['a','v','t','y','q','m']

print(len(numbers)) # eleman sayısı verir


value = min(numbers)
value1 = max(numbers)
print(value)
print(value1)

numbers[3] = 34 # güncelleme
print(numbers)

numbers.append(88) # ekleme işlemi
numbers.insert(2,24) # 2. indexe 24 elemanını ekledik. istediğimiz yere ekleme işlemi
print(numbers)

numbers.pop(8) # 8. indexteki eleman silindi
index =numbers.index(52) # index numarası öğrenme
print(index)
numbers.remove(24) # 24 elemanını silecek
numbers.sort() # küçükten büyüğe sıralama
numbers.reverse() # büyükten küçüğe sıralama
numbers.clear() # elemanları temizler
print(numbers)