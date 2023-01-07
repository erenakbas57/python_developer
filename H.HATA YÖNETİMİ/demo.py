

"""
1- liste elemanları içindeki sayısal değerleri bulunuz

2- kullanıcı q değerini girmedikçe aldığınız değerin sayı olduğundan
emin olunuz aksi halde hata mesajı yazınız

3- girilen parola içinde türkçe karakter hatası veriniz

4- faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için 
hata mesajları veriniz 
"""

# 1-
"""
liste = ["1","2","5a","10b","abc","10","50"]
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
"""
# 2-
"""
while True:
    sayi = input("sayı : ")
    if sayi == "q":
        break

    try:
        result = float(sayi)
        print(f"girdiğiniz sayı : {result}")
    except ValueError:
        print("geçersiz sayı")
        continue
"""
# 3-
"""
def check_password(parola):
    turkce_karakterler = "ğüşöçıĞÜÖÇŞİ"
    for x in parola:
        if x in turkce_karakterler:
            raise TypeError("parola türkçe karakter içeremez.")
        else:
            pass
    print("geçerli parola")

parola = input("parola giriniz : ")
try:
    check_password(parola)
except TypeError as te:
    print(te)
"""
# 4-
"""
def faktoriyel(deger):
    deger = int(deger)
    import re
    if deger<0:
        raise ValueError("negatif değer girdiniz")

    result = 1

    for i in range(1,deger+1):
        result = result * i
    return result

for y in [5,10,25,"a",-5]:
    try :
        x = faktoriyel(y)
    except ValueError as error:
        print(error)
        continue
    except Exception as error:
        print(error)
        continue
    print(x)
"""
