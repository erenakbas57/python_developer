from datetime import  *


result = datetime.now()  # tarih ve saati saniyesine kadar verir
# 2021-05-15 01:38:22.197663



simdi = datetime.now()

yil = simdi.year
month = simdi.month
hour = simdi.hour
minute = simdi.minute
second = simdi.second

result1 = datetime.ctime(simdi)
#Sat May 15 01:45:20 2021

"""
result2 = datetime.strftime(simdi,"%Y") # YIL 2021
result3 = datetime.strftime(simdi,"%y") # YIL 21

result4 = datetime.strftime(simdi,"%X") # SAAT 01:52:36

result6 = datetime.strftime(simdi,"%D") # TARİH 05/15/21
result7 = datetime.strftime(simdi,"%d") # DAY 15

result8 = datetime.strftime(simdi,"%A") # DAY SATURDAY
result9 = datetime.strftime(simdi,"%a") # DAY SAT

result10 = datetime.strftime(simdi,"%B") # AY MAY
result11 = datetime.strftime(simdi,"%b") # AY MAY


print(f"{result7}/{result10}/{result2}")
"""


#****************************************************************
"""
tarih = "15 April 2021 02:04:00"
dt = datetime.strptime(tarih,"%d %B %Y %H:%M:%S")
deger = dt.month

print(deger)
"""
#*****************************************************************

birthday = datetime(2001,11,2,6,5,52)
print(birthday)

deger = datetime.timestamp(birthday) # date to second
deger1 = datetime.fromtimestamp(deger) # second to date

deger2 = simdi - birthday
print(deger2)

#********************************************************************

asd = simdi + timedelta(days=10) # 10 gün ekler
dsa = simdi - timedelta(hours=856) # 856 saat çıkarır

print(dsa)