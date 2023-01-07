ogrenciler = {}

# bilgileri girerek iç içe bilgileri girdik
number = input("öğrenci no : ")
name = input("öğrenci ad : ")
surname = input("öğrenci soyad : ")
phone = input("öğrenci tel : ")

ogrenciler[number] = {
     'ad' : name,
     'soyad' : surname,
     'telefon' : phone
}
"""
 '384': {
    'ad': 'eren',
    'soyad': 'akbaş',
    'telefon': '05379234261'}
"""

print (ogrenciler)

# numara alarak öğrenci bilgilerini getirme
ogrNo = input('öğrenci no giriniz : ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

