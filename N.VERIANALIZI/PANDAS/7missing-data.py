import pandas as pd
import numpy as np

data = np.random.randint(0,100,15).reshape(5,3)

df = pd.DataFrame(data, index= ['a','c','e','f','h'], columns= ["column1","column2","column3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

newColumn = [np.nan,30,np.nan,51,23,np.nan,np.nan,76]
df["Column4"] = newColumn


result = df

result = df.drop("column1",axis=1) #axis 1 sütunu temsil eder.
result = df.drop("a",axis=0) #axis 0 satırı temsil eder

result = df.isnull() # NaN ola alanlar True gelir. bool değer döner
result = df.notnull() # sayı değeri olanlar True gelecek. bool değer

result = df.dropna() # axis = 0   ==> satıra (içinde null değer olan satırlar silindi)
result = df.dropna(axis=1) #sütun (içinde null değer olan sütunlar geldi)

result = df.dropna(how="all") #satırın hepsi null değer ise silinir
result = df.dropna(how="any") # satırda herhangi bir tane null değeri varsa silinir

result = df.dropna(subset=["column1","column2"],how="all")

result = df.dropna(thresh=2) # thresh ile "en az 2 tane normal veri olması gerek" dedik

result = df.fillna(value="Değer Yok") # NaN olan veriler doldurmak için


result = df.sum()
result = df.sum().sum()
result = df.size

result = df.isnull().sum()
result = df.isnull().sum().sum()
result = df



def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam /adet

print(result)
ort = df.fillna(value=ortalama(df))
print(ort)
