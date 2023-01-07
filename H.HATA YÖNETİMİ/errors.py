#   ERROR

#print(a) => NameError
#int("1a3") => ValueError
#print(10/0) => ZeroDivisionError
#print("denem"e) => SyntaxError


#   ERROR HANDLİNG
"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)
except ZeroDivisionError:
    print("0'a bölünme hatası. Y sayısı 0 değerini alamaz")
except ValueError:
    print("geçersiz değer girdiniz")
"""


"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)
except:
    print("geçersiz değer girdiniz...")
else:
    print("herhangi bir hata yok")    
# bu işlemde genel hata olduğu içn hata ayrıntısı ve ismini alamayız ve loglama yapamayız
"""

"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)
except (Exception) as ex:
    print("geçersiz değer girdiniz...", ex)
# Loglama yapılabilir. exception türünü de verdik    
"""

