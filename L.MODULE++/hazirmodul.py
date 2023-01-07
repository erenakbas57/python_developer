# Hazır Math Modülü
#   YÖNTEM 1

import math as matematik # as ile takma isim verdik

#value = dir(math) # math modulunun içindeki bütün func ları görürüz
#value = help(math.factorial) # math modulunun methodları hakkında bilgi alınır

value = matematik.sqrt(49) # kaç sayısının karesi
value = matematik.factorial(5)
#print(value)

#   YÖNTEM 2
from math import *

deger = factorial(5)
#print(deger)


# Hazır Random Modülü
import  random

resultrandom = random.random() # varsayılan 0.0 ile 1.0 arasında random sayı üretir
resultrandom = random.uniform(1,100) #baş ve bit değerleri girilerek sayı üretir. (ondalıklı)
resultrandom = random.randint(1,100) #baş ve bit değerleri ile tam sayı üretme
print(resultrandom)

names = ["eren","ahmet","salih","melike","asiye","kemal"]
deger1 = names[random.randint(0,len(names)-1)]
print(deger1)

deger2 = random.choices(names) # liste içerisinden rastgele eleman getirmek için choice methodu

liste = list(range(10)) # 0 dan başlayan 10 elemanlı liste
random.shuffle(liste) # orjinal listenin elemanlarının yerlerini kalıcı olarak değiştirir

liste1 = range(100)
deger3 = random.sample(liste1,5) # belirtilen liste içinden belirtilen adet kadar öğe getirir

print(deger3)