name = "EREN"
surname = "AKBAŞ"
age = 18


print("my name is {} {} . ı'm {} years old" .format(name,surname,age))
# my name is EREN AKBAŞ . ı'm 18 years old
print("my name is {n} {s}" .format(n=name,s=surname))
# my name is EREN AKBAŞ
print("my name is {0} {1}" .format(name,surname))
# my name is EREN AKBAŞ

print(f"my name is {name} {surname} . ı'm {age} years old") # başına f koyarak değişkenleri yerine yazabiliriz


result = 8000/423
result = round(result,2) # sayının ondalık kısmında 2 basamak gösterdi

print("sonuç : {}" .format(result))
