# value types => string number
x=5
y=25

x=y

y=10
#y 10 oldu x 25 değişiklikten etkilenmedi farklı adreslerde tutuluyor
print(x,y)

# reference types => list

a = ["elma","armut"]
b = ["elma","armut"]

a=b

b[0] = "karpuz"

# reference type olduğu için değişkenler güncellendi

print(a,b)