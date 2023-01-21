import numpy as np

numbers1 = np.random.randint(0,26,6)
numbers2 = np.random.randint(0,26,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 - numbers2
# dört işlem yapılır ve yeni dizi oluşur

result = np.sin(numbers1)
result = np.sqrt(numbers1) # karekökünü alır
result = np.log(numbers1) # logaritmasını alır

#############################################################

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
#print(mnumbers2)

result = np.vstack((mnumbers1,mnumbers2)) # dikey matris birleştirme
result = np.hstack((mnumbers1,mnumbers2)) # yatay matris birleştirme
print(result)
result = numbers1 >5
result = numbers1 % 2 ==0

print(numbers1[result]) # true olan değerleri ekrana yazar

print(result) # boolean değer döner (true , false)

