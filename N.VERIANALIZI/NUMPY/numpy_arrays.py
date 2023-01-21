import numpy as np

result = np.array([1,3,5,7,9])

result = np.arange(1,10)  # son eleman dahil değil
result = np.arange(0,100,3) # 0dan 100e kadar üçer üçer
result = np.zeros(5) # 5 tane sıfır

result = np.ones(5) # 5 tane bir

result = np.linspace(0,100,5) #0-100 arasını 5 eşit parçaya böldük

result = np.random.randint(0,10) # random sayı
result = np.random.randint(0,10,3) # 3 tane random sayı

#0-1 arası random sayı
result = np.random.rand(5)
result = np.random.random(5)


np_array = np.arange(50)
np_multi = np_array.reshape(5,10) # 5 satır 10 sütun yaptık
#print(np_multi)
#print(np_multi.sum(axis=1)) # satırların toplamı
#print(np_multi.sum(axis=0)) # sütunların toplamı


rnd_numbers = np.random.randint(0,101,5) # integer random
print(rnd_numbers)
print(rnd_numbers.max()) # max değer
print(rnd_numbers.min()) # min değer
print(rnd_numbers.mean()) # ortalaması
print(rnd_numbers.argmax()) # max değerin indexi
print(rnd_numbers.argmin()) # min değerin indexi
