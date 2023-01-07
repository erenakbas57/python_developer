# fonksiyonlar bir objedir


"""
def ornek(name):
    print(f"merhaba {name}")

hello = ornek

ornek("eren")
hello("melike")
print(ornek)
print(hello)
# ikiside bellekte aynı adresi tutar
"""


#**********************************************
"""
#encapsulation
def outer(num1):
    print("outer func")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1 , num2)

outer(10)
"""
#**********************************************

"""
def faktoriyel(number):
    if not isinstance(number,int):
        raise TypeError("Tam sayı değeri girilmelidir")
    if number<=0:
        raise ValueError("Değer 0 dan büyük olmalıdır")

    def inner_factorial(number):
        import math
        if number<=1:
            return 1

        return math.factorial(number)

    return inner_factorial(number)

try:
    print(faktoriyel(5))
except Exception as ex:
    print(ex)

"""