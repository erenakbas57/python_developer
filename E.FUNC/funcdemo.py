"""
1-gönderilen kelimeyi belirtilen kez ekranda yazdıran func
2-kendine gönderilen sınırsız sayıdaki parametreyi listeye çeviren func
3-kendisine gönderilen sayının tam bölenlerini bulan func
"""

#1-
def loop():
    word = input("kelimeyi giriniz : ")
    loop = int(input("kaç kere ekrana yazılsın : "))
    bas=1
    while bas<=loop:
        print(word)
        bas+=1
#loop()

#2-
def myList(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

#print(myList(1,2,3,4,5,6,7,8,9))

#3-
def tamBolen():
    sayi = int(input("sayıyı giriniz : "))
    tambolenler= []
    for i in range(1,sayi+1):
        if (sayi%i==0):
            tambolenler.append(i)
        else:
            continue
    print(list(tambolenler))

#tamBolen()