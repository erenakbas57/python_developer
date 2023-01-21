import pandas as pd

# customers = {
#     'CustomerID' : [1,2,3,4],
#     'FirstName'  : ["Ahmet","Ali","Hasan","Canan"],
#     'LastName'   : ["Yılmaz","Korkmaz","Celik","Toprak"] 
# }

# orders = {
#     'OrdersID'   : [10,11,12,13],
#     'CustomerID' : [1,2,5,7],
#     'OrderDate'  : ['2010-07-04','2010-08-04','2010-07-07','2012-07-04'] 
# }

# df_customers = pd.DataFrame(customers, columns=["CustomerID","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns= ["OrdersID","CustomerID","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how="inner") # inner join ile siparişi olan tüm müşteriler geldi
# result1 = pd.merge(df_customers,df_orders,how="left") # left join ile NaN olan müşteriler de gelir

# print(result)
# print(result1)

#-----------------------------------------------------------------------------

customersA = {
    'CustomerID' : [1,2,3,4],
    'FirstName'  : ["Ahmet","Ali","Hasan","Canan"],
    'LastName'   : ["Yılmaz","Korkmaz","Celik","Toprak"] 
}

customersB = {
    'CustomerID' : [5,6,7,8],
    'FirstName'  : ["Yagmur","Cinar","Cengiz","Can"],
    'LastName'   : ["Bilge","Turan","Yilmaz","Turan"] 
}

df_customersA = pd.DataFrame(customersA, columns=["CustomerID","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns=["CustomerID","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB],axis=0)

print(result)