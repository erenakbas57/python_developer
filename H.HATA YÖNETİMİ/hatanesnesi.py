# Kendi hata nesnesini oluşturma

# basit örnek
"""
x=10
if x >5:
    raise Exception("x 5'ten büyük değer alamaz")
"""

# örnek
"""
def check_password(psw):
    import re
    if len(psw) <8:
        raise Exception("Parola en az 8 karakter içermelidir")
    # search ile paroladaki değerleri arama yaparız
    elif not re.search("[0-9]",psw):
        raise Exception("Parola rakam içermelidir")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola en az bir küçük rakam içermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola en az bir büyük rakam içermelidir")
    elif not re.search("[!'^^+%&/()=?_~¨´>£#$$<½*|]",psw):
        raise Exception("Parola alpha numerik karakter içermelidir")
    elif re.search("\s",psw):
        raise Exception("Parola boşluk içermemelidir")
    else:
        print("parola oluşturulabilir")

password = "Erenasd123_"

try:
    check_password(password)
except Exception as ex:
    print(ex)
"""

#Class örneği

class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("isim alanı fazla karakter içeriyor")
        else:
            self.name = name

p = Person("muhammedalibekar",1990)