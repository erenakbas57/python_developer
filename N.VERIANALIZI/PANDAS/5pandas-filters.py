import pandas as pd
import numpy as np

datarandom = np.random.randint(0,100,75).reshape(5,15)

data = {
    "name" : ["eren","ali","selim","salih","yavuz","abdulhamid","osman","orhan","bayezid","vahdeddin","abdulaziz","mehmed","murat","mete","kamil"],
    "older" : [20,18,45,42,63,85,38,32,19,27,29,30,52,57,40],
    "city" : ["istanbul","bursa","kütahya","kastamonu","rize","trabzon","malatya","edirne","kocaeli","sakarya","sinop","ankara","izmir","adana","antalya"],
    "job" : ["student","goverment","engineer","doctor","secretary","student","architect","student","goverment","engineer","doctor","secreter","student","doctor","engineer"],
    "gender" : ["male","male","male","male","male","male","male","male","male","male","male","male","male","male","male"]
}

df = pd.DataFrame(data)

result = df
result = df.columns # kolon isimlerini alır
result = df.head() #otomatiği 5tir. içine kaç yazarsak baştan o kadar veri gelir
result = df.tail() #otomatiği 5tir. içine kaç yazarsak sondan o kadar veri gelir

result = df["name"].head() # ilk 5 satırın column1 lerini gösterir

result = df[["name","older"]].head() #biden fazla kolon için tekrar köşeli parantez içinde belirtilir

result = df[5:15][["name","older","city"]].head()
#indexi 5-15 arasında olan 5 sonucun "name , older , gender " sütunları ve verileri gelir

#result = df >50
#bu işlemde boolean değer döner. ama bizim dataframede yazılarda olduğu için hata verir

result = df[df["older"]>30] # 30dan büyük olan kişiler
result = df[df["older"]>30][["name","older","city"]]
result = df[(df["older"] <50) & (df["older"]>30)]
result = df[(df["older"] <50) & (df["older"]>30)][["name","older"]]


#print(result)