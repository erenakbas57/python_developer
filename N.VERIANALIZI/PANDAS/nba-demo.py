import pandas as pd
import numpy as np

data = pd.read_csv("./dataset/znba.csv")


#1- ilk 10 kayıtı getir
result = data.head(10)

#2- toplam kayıt sayısı
result = len(data.index)

#3- tüm oyuncuların toplam maaş ortalaması

result = data["Salary"].mean()

#4- en yüksek maaş ne kadardır
result = data["Salary"].max()

#5- en yüksek maaşı alan oyuncu
result = data[data["Salary"]==data["Salary"].max()]["Name"]

#6- yaşı 20-25 arasımda olan oyuncuların isimleri ve mevkileri
result = data[(data["Age"]>=20) & (data["Age"]<=25)][["Name","Position"]]

#7- "John Holland" oynadığı takım
result = data[(data["Name"] == "John Holland")]["Team"]

#8- Takımlara göre oyuncuların ortalama maaş bilgisi
result = data.groupby("Team").mean()["Salary"]

#9- kaç farklı takım mevcut
result = len(data.groupby("Team"))

#10- her takımda kaç oyuncu oynamakta
result = data["Team"].value_counts()


#11- ismi içinde "and" geçen kayıtları bul




print(result)