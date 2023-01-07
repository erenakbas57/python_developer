import os

#result = dir(os) # işletim sistemi ile ilgili modul

#print(result)


#deger = os.name   işletim sistemi name
#deger = os.getcwd() şuanki dizinin konumunu gösterir


#print(deger)


#os.chdir("C:\\")  dizin değiştirme
#os.chdir("..")  bir üst dizine geçer


#os.mkdir("newdirectory1") # bulunan klasör altına yeni klasör oluşturur
#os.makedirs("newfolder/yeniklasor") klasör oluşturma iç içe
#os.rename("newdirectory","yeniklasor") isim değiştirme
#os.rmdir("newdirectory") klasör silme
#os.removedirs("yeniklasor/yeniklasor") içi dolu klasörleri silme


#print(os.listdir()) dizindeki klasörün içindeki dosyaları listeler.
#print(os.listdir("C:\\")) parantez içine yazılan konumu listeler


#os.stat("_os.py") dosya hakkında bilgi edinilir
#os.system("notepad.exe") belirtilen dosya açılır



#PATH

#result = os.path.abspath("_os.py") belirtilen dosyanın tam konumunu verir
#result = os.path.dirname((os.path.abspath("_os.py")))
# ilk dosyanın tam konumunu buldu ve sonra dizinini buldu

#result = os.path.exists("_os.py") bulunan dizinde belirtilen dosyanın varlığını kontrol ediyor

#os.path.isdir("_os.py")  belirtilen dizi veya dosyanın klasör olup olmadığını kontrol eder
# os.path.isfile("_os.py") doosya olup olmadığını kontrol eder

#result =os.path.join("C:\\","deneme","deneme1") dizin birleştirme
#result = os.path.split("C:\deneme") ayırma
#result = os.path.splitext("_os.py") isim ve uzantıyı ayırır

