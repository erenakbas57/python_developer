# break : ile işlem durdurulur (kırılır)
#continue : ile işlem es geçilir (yapılmaz)

name = 'EREN AKBAŞ'
for letter in name:
    if (letter==' '):
        break  # EREN ifadesi yazdıktan sonra döngü kırıldı ve program durdu
    else:
        print(letter)

word = 'eren akbaş'
for letter1 in word:
    if (letter1=='e'):
        continue # bu işlemde ise döngüde e harfine geldiği zaman işlem yapılmadan es geçiliyor
    else:
        print(letter1)


#1-100 arası tek sayıların toplamı
x=0
toplam=0
while (x<=100):
    x+=1
    if (x%2==0):
        continue
    else:
        toplam+=x

print(toplam)