list1 = ['eren', 3, True, 6.1]
list2 = ('eren', 3, True, 6.1)

a = ['selim', 23]
b = 'selim', 23

print(type(list1)) #list türü
print(type(list2)) # tuple türü

# tuple elemanları sonradan değiştirilmez

c = list1 + a
d = list2 + b

print(c)
print(d)