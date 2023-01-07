#bankamatik demo

ErenHesap = {
    'Ad' : 'Eren Akbaş',
    'HesapNo' : '202051501008',
    'Bakiye' : 650,
    'KrediKarti' : 1300
}
MelikeHesap = {
    'Ad' : 'Melike Akbaş',
    'HesapNo' : '202151473004',
    'Bakiye' : 925,
    'KrediKarti' : 2400
}

def ParaCekme(hesap,miktar):
    print(f"Merhaba {hesap['Ad']}")

    if (hesap['Bakiye'] >= miktar):
        hesap['Bakiye'] -=miktar
        print("Paranızı alabilirsiniz...")
    else:
        toplam = hesap['Bakiye'] + hesap['KrediKarti']

        if (toplam>=miktar):
            print("Ana hesabınızın bakiyesi yetersiz.")
            while(True):
                ekHesapKullanimi = input("Kredi Kartı kullanılsın mı ? (e/h) : ")

                if (ekHesapKullanimi == 'e'):
                    KrediKartiKullanilacakMiktar= miktar - hesap['Bakiye']
                    hesap['Bakiye'] = 0
                    hesap['KrediKarti'] -= KrediKartiKullanilacakMiktar
                    print("Paranızı alabilirsiniz..."),
                    break
                elif (ekHesapKullanimi == 'h'):
                    print(
                        f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} bakiye bulunmaktadır.\nHesabınızdan çıkış yapılıyor...")
                    break
                else:
                    print("Hatalı giriş yaptınız.")
                    continue
        else:
            print("Üzgünüm bakiyeniz yetersiz...\nHesabınızdan çıkış yapılıyor...")

def BakiyeSorgulama(hesap):
    print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} TL bulunmaktadır.\nKredi kartı nakit avans limitiniz ise {hesap['KrediKarti']} TL'dir.")


ParaCekme(MelikeHesap,3000)
BakiyeSorgulama(MelikeHesap)