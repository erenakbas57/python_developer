# range(başlangıç,bitiş,artış)

print(list(range(0,25,2))) # 0dan 25e kadar ikişer ikişer artan bir liste

# enumerate ile string ifadelerin her harfini (index,string harf değeri) olacak şekilde dizi haline getirir

hey = 'hello'
for index,letter in enumerate(hey):
    print(f' index : {index} ve harf : {letter}')


# zip ile örneğin ii listeyi dicyionary gibi birleştirmeye yarar

number = [1,2,3,4,5]
name = ['eren','mahmut','mehmet','ali','halit']
country = ['istanbul','izmir','aydın','bursa','kastamonu']
list = list(zip(name,number,country))
print(list)

# comprehensions

numbers = [x for x in range(10)]
#range döndükçe 0 dan başlayarak 10 adet değer üretecek ve her dönen değeri x değişkeninin içine atarak
#numbers dizisine eleman olarak append edecek
print(numbers)

list1 = [y*y for y in range(10) if y%3==0]
print(list1)

#********************************************
myString = 'hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)

# daha kolay hali

myList =[letter for letter in myString]
print(myList)