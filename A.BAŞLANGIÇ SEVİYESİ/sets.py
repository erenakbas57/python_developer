fruits = {'orange', 'banana', 'apple'}
print(type(fruits))
print(fruits)  # indexlenemez

for fruit in fruits: 
    print(fruit)

fruits.add('cherry') # tekli ekleme işlemi
fruits.update(['mango','melon','apple']) # çoklu liste şeklinde ekleme. olan eleman tekrar eklenemez. 

print(fruits)

fruits.remove('mango')  #silme methodu
fruits.discard('melon') # silme methodu

print(fruits)
fruits.clear() # temizler

fruits.add('melon')
print(fruits)

mylist = [1,2,3,4,2,3,1,2,2]
print(set(mylist))  #set ile tekrarlayan elemanları yazdırmadık


