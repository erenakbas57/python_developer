message = 'Hello there. My name is Eren'.split()
print(message)

myList = [1,2,3,4,5,6,7,8,9,0]
myList2 = ['eren',2,True,3.6]

print(myList)
print(myList[0])
print(len(myList)) # len ile dizinin eleman sayısı bulunur
print(set(myList))  #set ile tekrarlayan elemanları yazdırmadık


userA = ['Eren',36]
userB = ['Ali',34]
users = userA + userB # 4 elemenalı dizi oldu
allusers = [userA,userB] # iç içe dizi oldu

print(users)
print(allusers)
print(allusers[0][0]) # iç içe dizinin 0. elemanının 0. elemanı eren dir
print(type(myList2))
