"""
file = open("fileread.txt","r",encoding="utf-8")
content = file.read()
print(content)
"""

#alternative

with open("fileread.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(file.tell()) #dosyada kursörün konumunnu verir
    file.seek(0) # kursörü nereye götüreceğimi yapan func
    print(file.tell())
    print(file.read())



    #sonuna gelince otomatik open kapanacak. close yapmaya gerek yok