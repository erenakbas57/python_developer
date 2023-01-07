# is
#bir şeyi karşılaştırırken nesnelere değil obje karşılaştırması yapar

x = [1,2,3]
y = [1,2,3]

#print(x==y)   #x ve y değerleri eşittir : true
#print(x is y)  # x ve y farklı referanslara sahip olduğu için eşit değildir : false

# in
#bir şeyin içinde olup olmadığını kontrol etmek için kullanılır

fruit = ["banana","apple"]
print("apple" in fruit)
name = "eren"
print('r' in name)