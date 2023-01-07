# fonksiyonlar

def sayHello(name='user'):
    print(f"Hello {name}")
#sayHello('Eren')


def sayHi(name1 ='user'):
    return 'hello ' + name1
msg = sayHi('Eren')
#print(msg)

def Toplam(sayi1,sayi2):
    return  sayi1 + sayi2
result = Toplam(15,64)
#print(result)

def yasHesapla(dogumYili):
    return 2021-dogumYili

def emekliligeKacYilKaldi(dogumYili,isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65-yas

    if (emeklilik>0):
        print(f'emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print('zaten emeklisiniz')

#emekliligeKacYilKaldi(2001,'eren')


#*************************************
def Topla(*a): # * tek yıldız tuple ifade eder. tuple(listenin farklı türü) ifade ettiği için params gibi kullanılır.
    return sum((a))

#print(Topla(1,2,3,4,5,6,7,8,9))


def userFile(**dicargs): # ** çift yıldız dictionary ifade eder. key value değerleri girilir
    for key,value in dicargs.items():
        print(f'{key} : {value} ')

userFile(name='eren',age=15,country='İstanbul')

def myFunc(a,*b,**c):
    print(a)
    print(b)
    print(c)

myFunc(14,1,2,3,4,5,6,7,8,9,name='eren',age=19)