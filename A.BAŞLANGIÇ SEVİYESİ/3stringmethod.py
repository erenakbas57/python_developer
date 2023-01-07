message = "my name is Eren . Im 19 years old"

#message = message.upper()

#message = message.split('.') # string ifadeyi noktalardan itibaren ayırır

# upper methodu bütün harfleri büyük yapar
# lower methodu bütün harfleri küçük yapar
# tıtle methodu ile bütün kelimelerin baş harfi büyük olur
# capitalize methodu ile string ifadenin sadece ilk harfi büyük olur

# strip methodu ile başta ve sondaki boşluk karakterlerini siler
website = "https://www.instagram.com"
website = website.lstrip('/:htps') # website değişkeni içinde sadece soldan itibaren tırnak içindeki karakterleri sildi
print(website)

# split ile her kelimeyi parçaya dönüştürür.

#join methodu ile parçaları tekrar birleştirir
message = message.split()
message = ' '.join(message)

# replace methodu ile bir ifadeyi başka ifade ile değiştiririz
message = message.replace('Eren','Muhammed eren akbaş') # eren ifadesi yerine muhammed eren akbaş geldi


print(message)