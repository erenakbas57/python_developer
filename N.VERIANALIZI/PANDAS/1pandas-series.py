import pandas as pd
import numpy as np
import math

#data
numbers = [10,20,30,40,50]
letters = ["a","b","c","d","e"]
mixed = ["a","b",10,20,"e"]
dict = {"a":10,"b":20,"c":30,"d":40}
random_numbers = np.random.randint(0,100,15)

pandas_series1 = pd.Series(numbers)                             #int64
pandas_series2 = pd.Series(letters)                             #object
pandas_series3 = pd.Series(mixed)                               #object
pandas_series4 = pd.Series(numbers, ["a","b","c","d","e"])      # 2.değişken indeks
pandas_series5 = pd.Series(dict)                                # dictionary pandas yapısına sahiptir
pandas_series6 = pd.Series(random_numbers)                      #int64


print(pandas_series4)           # indeksli tablo gelir

result = pandas_series4[0] # 0. indeks
result = pandas_series4[-1] # sonuncu indeks
result = pandas_series4[:2] # 2. indekse kadar gelir. (dahil değildir)
result = pandas_series4[-2:] # sondan 2 tane
result = pandas_series4["a"] # a indeksindeki değer
result = pandas_series4[["a","c"]] # a ve c indeksleri gelir

result = pandas_series4.dtype

result = pandas_series4.ndim  #kaç  boyut olduğunu söyler
result = pandas_series4.shape # boyuta göre eleman sayısı (2,4) gibi

result = pandas_series4.sum() # toplama
result = pandas_series4.max() 
result = pandas_series4.min()

result = pandas_series4 * 2         # böyle işlemlerde tüm değerler için işlem yapılır

result = np.sqrt(pandas_series4)    # karekök alma

result = pandas_series4 <=30        # her değer yerine true false döner



opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total = opel2018 + opel2019 # örnek astra iki tabloda da var. toplanır yeni tablo olur. olmayanlar "NaN" olur
#print(total)
#print(total["astra"])

