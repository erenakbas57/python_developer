#R (read) : okuma modu -->  VARSAYILAN

#dosya konumda yoksa hata verir.

file = open("fileread.txt","r",encoding="utf-8")

# dosyadaki her satırı sırayla yazar.
"""
for i in file:
    #print(i, end="")
file.close()
"""

#alternative
"""
result = file.read()
print(result)
file.close()
"""


"""
file = open("fileread.txt","r",encoding="utf-8")
content = file.read()
print("***  içerik 1  ***")
print(content)

file = open("fileread.txt","r",encoding="utf-8")
# eğer bu satır olmasaydı içerik tekrar yazdırılmazdı. çünkü
# kursör dosyanın sonunda olduğu için okunacak bir şey kalmazdı
content2 = file.read()
print("***  içerik 2  ***")
print(content2)
"""


"""
deger = file.read(5) # beş karakteri okur
deger = file.read(5) # sonraki beş karakteri okur
print(deger)
"""


"""
print(file.readline(), end="") # satırı okur.
print(file.readline(), end="")
print(file.readline(), end="")
"""


liste = file.readlines() # her satırı bir liste elemanı şeklinde okur
print(liste)


file.close()