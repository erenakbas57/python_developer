import pandas as pd
import sqlite3

df = pd.read_csv("zdeneme.csv")

df = pd.read_json("zdeneme.json",encoding="utf-8")

df = pd.read_excel("zdeneme.xlsx")
#print(df)
# excel okumak için xlrd kütüphanesini indirdik



connection = sqlite3.connect("zdeneme.db")                  #dosyayla bağlantı
df =pd.read_sql_query("SELECT * FROM users",connection)     #sql komutları
#database okumak için pysqlite3 kütüphanesini kurduk

print(df)