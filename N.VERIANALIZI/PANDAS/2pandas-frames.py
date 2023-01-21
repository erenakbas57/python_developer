import pandas as pd

#df = pd.DataFrame()
#df = pd.DataFrame([1,2,3,4])

list = [["ahmet",50],["ali",60],["yağmur",70],["çınar",60], ["eren",80]]
dict = {"name": ["ahmet","ali","deniz","fırat","çakır"],
        "older": [18,20,42,15,32] }
dict_list = [{"name":"ahmet","older":18},
             {"name":"ali","older":35},
             {"name":"hasan","older":75},
             {"name":"selim","older":12},
             {"name":"hatice","older":42}
             ]

df = pd.DataFrame(list, columns=['İsim','Puan'],index= [1,2,3,4,5])
#print(df)
df = pd.DataFrame(dict)
#print(df)
df = pd.DataFrame(dict_list)
#print(df)



"""
s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1 , oranges = s2)

df = pd.DataFrame(data)

print(df)
"""