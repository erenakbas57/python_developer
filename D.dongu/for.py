numbers = [1,2,3,4,5,6,7,8,9,0]

for number in numbers:
    print(number)

print("***************************************")


name = 'Eren Akbaş'

for n in name :
    print(n)        # string liste gibi her harfi tek tek yazar


print("***************************************")


List = [[1,2],[1,3],[1,4]]

for t,v in List:
    print(t,v)
print(type(List))

print("***************************************")


dictionary = {'k1':1,'k2':2,'k3':3}

for key,value in dictionary.items():
    print(value)