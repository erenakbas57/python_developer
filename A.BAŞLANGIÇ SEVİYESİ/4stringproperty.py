web = "www.instagram.com and www.facebook.com"
course = "python programlama dersleri temel orta ileri seviye"

name, surname,age,job = "eren","akbaş",19,"öğrenci"

print(f"merhaba benim adım {name} {surname}. {age} yaşındayım. mesleğim {job}")

print(" ")

print(len(web))
# len özelliği ile string uzunluğu bulunur

print(web[4:13]) 
#yazı içerisinde 4 ve 13 index arasındaki harfleri aldık

print(course[::-1])
# string ifadeyi tersten yazdırdık

result = "abc " * 3
print(result)
