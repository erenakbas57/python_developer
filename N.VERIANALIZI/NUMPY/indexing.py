import numpy as np


numbers = np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])

result = numbers[1]
result = numbers[:3] #0.indexten 3. indexe kadar
result = numbers[::] # bütün listeyi alır
result = numbers[::-1] # bütün listeyi sağdan sola alır

numbers1 = np.array([[3,6,9],[12,15,18],[21,24,27]])
result = numbers1[0]
result = numbers1[0,2] # 0. indexin içindeki 2.indexi alır yani "9"

result = numbers1[:,1] # her elemanı seçtik , 1 ile de her elemanın içindeki 1. indexi seçtik

result = numbers1[:,0:2] # her elemanda 2.indexe kadar alacak (2,İNDEX DAHİL DEĞİL)

########################################################

arr1 = np.arange(0,10)
arr2 = arr1   # referans

arr2[0] = 20
# arr1 de 0. indexi 20 ile güncellendi. çünkü hafızada ikiside aynı adresi tutuyor.

print(arr1)
print(arr2)

########################################################

array1 = np.arange(0,10)
array2 = array1.copy()

array2[0] = 20
# değişiklik array1 i etkilemedi

print(array1)
print(array2)

########################################################

#print(result)