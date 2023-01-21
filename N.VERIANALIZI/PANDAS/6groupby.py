import pandas as pd
import numpy as np

personeller = {
    "Calisan" : ["Ahmet Yilmaz","Can Erturk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Riza Erturk","Mustafa Can"],
    "Departman" : ["Insan Kaynaklari","Bilgi Islem","Muhasebe","Insan Kaynaklari","Bilgi Islem","Muhasebe","Bilgi Islem"],
    "Yas" : [30,25,45,50,23,34,42],
    "Semt" : ["Kadikoy","Tuzla","Maltepe","Tuzla","Kadikoy","Tuzla","Maltepe"],
    "Maas" : [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
result = df


result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups # indeks bilgilerinin çıktısını verir


# .groups metodunu koymazsak sadeceobject ismi döndürür

# semtler = df.groupby("Semt")
# for name,group in semtler:
#     print(name)
#     print(group)
#     print("")


# for name,group in df.groupby("Departman"):
#     print(name)
#     print(group)
#     print("")

result = df.groupby("Semt").get_group("Kadikoy")
result = df.groupby("Departman").get_group("Muhasebe")

result = df.groupby("Departman").sum()
result = df.groupby("Maas").mean() # ortalama
result = df.groupby("Semt").count() # veri toplamı (sum ile sayıları topluyoruz matematiksel işlem)

result = df.groupby("Departman").agg(np.mean) # numpy üzerinden ortalama hesapladık

result = df.groupby("Yas")["Maas"].mean()
print(result)

result = df.groupby("Departman")["Maas"].agg([np.sum,np.mean,np.max,np.min])
print(result)
