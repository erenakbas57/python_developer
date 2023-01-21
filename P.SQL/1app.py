
import mysql.connector  as sql

def InsertProduct(name,price,imageUrl,description):
    connection = sql.connect(host = "localhost", user ="root", password = "1234", database = "node-app")
    cursor = connection.cursor()
    
    query = "INSERT INTO Products (name,price,imageUrl,description) VALUE (%s,%s,%s,%s)"
    value =  (name,price,imageUrl,description)

    cursor.execute(query,value)

    try:
        connection.commit()
    except sql.Error as err:
        print("Hata : ", err)
    finally:
        connection.close()
        print("Database closed...")

def InsertProducts(list):
    connection = sql.connect(host = "localhost", user ="root", password = "1234", database = "node-app")
    cursor = connection.cursor()
    
    query = "INSERT INTO Products (name,price,imageUrl,description) VALUE (%s,%s,%s,%s)"
    value =  list

    cursor.executemany(query,value)

    try:
        connection.commit()
    except sql.Error as err:
        print("Hata : ", err)
    finally:
        print(f"{cursor.rowcount} adet kayıt eklendi")
        connection.close()
        print("Database closed...")

product = []
while True:
    name = input("Ürün Adı : ")
    price = input("Ürün Fiyatı : ")
    imageUrl = input("Ürün Fotoğraf konumu : ")
    description = input("Ürün Açıklaması : ")

    product.append((name,price,imageUrl,description))

    result = input("veri girmeye devam edecek misiniz? (e/h) : ")
    if (result == 'h'):
        print("sorgu veritabanına akratılıyor...")
        InsertProducts(product)
        break
