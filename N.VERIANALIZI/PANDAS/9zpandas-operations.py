import pandas as pd
import numpy as np


# data = {
#     "Column1" : [1,2,3,4,5],
#     "Column2" : [10,20,13,20,25],
#     "Column3" : ["abc","bca","ade","cba","dea"]
# }

# df = pd.DataFrame(data)

# result = df["Column2"].unique


# def kareal(x):
#     return x * x

# result = df["Column1"].apply(kareal)
# print(df)
# print(result)

#--------------------------------------------------

data = {
    "Ay" : ["Ocak","Subat","Mart","Ocak","Subat","Mart","Ocak","Subat","Mart"],
    "Kategori" : ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir" : [12,34,75,52,84,26,12,93,43]
}

df = pd.DataFrame(data)

result = df.sort_values("Gelir").groupby("Ay").groups



print(result)