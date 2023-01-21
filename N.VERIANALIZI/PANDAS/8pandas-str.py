import pandas as pd

data = pd.read_csv("znba.csv")

data.dropna(inplace=True)


#data["Name"] = data["Name"].str.upper() # name kolonu bütün isimleri büyük harf yaptık
#data["Name"] = data["Name"].str.lower()
#data["index"] = data["Name"].str.find("a") # name kolonundaki a karakterinin kaçıncı indexte olduğunu yazar

#data = data[data.Name.str.contains('Jordan')]

#data = data.Team.str.replace(' ','-')

data[['FirstName','LastName']] = data['Name'].loc[data['Name'].str.split(' ').len()==2].str.split(expand=True)

print(data.head(10))