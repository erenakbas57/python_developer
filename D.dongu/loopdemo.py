#kullanıcının verdiği değerler arasında rastgele üretilecek sayıyı aşağı ve yukaru ifadeleri ile
#kullanıcıya buldurmaya çalışan program

'''
random modülü ile yapın
100 üzeriden puanlama yap. her soru 20 puan
hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısına göre hesaplansın
'''

import  random
#moduller import ile eklenir
bas = int(input('başlangıç değeri : '))
bit = int(input('bitiş değeri : '))
sayi = random.randint(bas,bit)
can = int(input('kaç hakkınız olsun : '))
hak =can
sayac =0

while (hak>0):
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin giriniz : '))
    if (sayi == tahmin):
        print(f'tebrikler! {sayac}. seferde tahmininiz doğru. \npuanınız : {100 - (100/can)*(sayac-1)} ')
        break
    elif (sayi > tahmin):
        print('yukarı')
    else :
        print('aşağı')

    if (hak==0):
        print(f'hakkınız bitti. Tutulan sayı {sayi} . \npuanınız : 0')
