import pandas as pd
from numpy.random import randn

dict_data = {
    "name" : ["eren","ahmet","salih"],
    "older" : [20,15,45],
    "school" : ["DPU","KATU","ITU"]
}


#df = pd.DataFrame(randn(3,3),index=["A","B","C"], columns=["Column1","Column2","Column3"])

df = pd.DataFrame(dict_data)


result = df
result = df["name"] #series
result = df[["name","older"]] # dataframe

# loc["row","column"] ==> loc["row"] ==> loc[":","column"]
result = df.loc[0]
result = df.loc[:,"name"]
result = df.loc[:,["name","older"]]


#burada kendi verdiğimiz indexleri kullandık. normal indexleri kullanmak istersek
result = df.iloc[:,:]

result = df.loc[1,"name"] # 1. indeksin name alanını verecek yani "ahmet"
result = df.loc[[0,1],["name","school"]] # 0. ve 1. indeksşn name and school bilgisi


df["city"] = pd.Series(["istanbul","ankara","bursa"]) # yeni kolon ekledik

result =df.drop("school",axis = 1) # drop ile kolon sildik. axis = 1 aşağıdan yukarıyı temsil ediyor
#result üzerindeki kopyasından silindi. orjinal df de kolon hala duruyor.

df.drop("school",axis=1,inplace=True)
#inplace i true yaparsak orjinal df dende silinecek


#print(result)
#print(df)
