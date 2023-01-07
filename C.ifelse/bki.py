kg = float(input("kilonuz : "))
boy = float(input("boyunuz : "))
boy = boy/100
bki = kg / (boy**2)

if (bki<=18.5):
    print(f"boy kilo indeksiniz {round(bki,2)} : ZAYIFSINIZ")
elif (bki>18.5 and bki<=24.9):
    print(f"boy kilo indeksiniz {round(bki,2)} : NORMALSİNİZ")
elif (bki>24.9 and bki<=29.9):
    print(f"boy kilo indeksiniz {round(bki,2)} : KİLOLUSUNUZ")
elif (bki>29.9 and bki<=34.9):
    print(f"boy kilo indeksiniz {round(bki,2)} : AŞIRI KİLOLUSUNUZ")
elif (bki>35):
    print(f"boy kilo indeksiniz {round(bki,2)} : OBEZSİNİZ")
else:
    print("geçersiz değer girdiniz")