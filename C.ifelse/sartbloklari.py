sayi1 = int(input("1. sayıyı giriniz : "))
sayi2 = int(input("2. sayıyı giriniz : "))

if sayi1 > sayi2:
    print(f"{sayi1} , {sayi2}'den büyüktür")
elif sayi2 > sayi1:
    print(f"{sayi2} , {sayi1}'den büyüktür")
else:
    print(f"{sayi1}={sayi2} , sayılar eşittir")

#************************************************

name = input("isim giriniz : ")
if name == 'eren':
    password = input("şifre giriniz : ")
    if password == '1234':
        print("hoşgeldiniz")
    else:
        print("parola yanlış")
else:
    print("isim yanlış")
