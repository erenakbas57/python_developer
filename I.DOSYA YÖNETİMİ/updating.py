"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    # r+ hem okuma hem yazma modu demektir
    file.seek(20)
    file.write("**NABER**")
    # 20.noktadan itibaren olan yazıyı değiştirdi

with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())
"""

#SAYFA SONU GÜNCELLEME İŞLEMİ
"""
with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nMelike Akbaş") #sayfa sonuna yazı ekledi

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
"""


#SAYFA BAŞI GÜNCELLEME İŞLEMİ
"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    content = file.read()
    content = "Hasan Akbaş\n" + content
    file.seek(0)
    file.write(content)


with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
"""


#SAYFA ORTASINDA GÜNCELLEME İŞLEMİ
"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    liste =file.readlines()
    liste.insert(1,"Zeynep Akbaş\n")
    file.seek(0)
    file.writelines(liste)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())

"""



