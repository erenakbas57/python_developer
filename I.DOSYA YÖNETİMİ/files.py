"""
dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
Kullanımı : open(dosya_adi,dosya_erisme_modu)
dosya erişme modu --> dosyayı hangi amaçla kullanacağımızı belirtir
"""

#W (write) : yazma modu -->

file =open("newfile.txt","w",encoding="utf-8")
file.write("eren akbaş 02.11.2001")
file.close()

# dosya içeriğini siler ve yeniden ekleme yapar
# konumda yeni dosya oluşturur



#A (append) : ekleme modu -->

file1 = open("fileappend.txt","a",encoding="utf8")
file1.write("202051501008")
file1.close()

#konumda dosya yoksa yeni oluşturur.
#dosya içeriğinin üzerine ekleme yapar



#X (create) : oluşturma modu -->

file2 = open("filecrate.txt","x")
file2.close()

#sadece dosya oluşturma işleminde kullanılır
#dosya zaten varsa hata verir



