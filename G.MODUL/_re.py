import re

# regular expression

str = "Python Kursu: python programlama temelleri | 40 saat"

#result = re.findall("Python",str) aranılan bilgileri liste şeklinde sunar

#result = re.split(" ",str) boşluk ifaderlerden sonra böler ve liste şeklinde verir

#result = re.sub(" ","-",str) değiştirme işlemi. boşluğu tire ile değiştirdi

#result = re.search("Python",str) #arama işlemi. match objesi ile döndürdü

#MATCH obje işlemleri
#result = result.span() # yerini belirtir (0,6)
#result = result.start() # başlangıç indexi
#result = result.end() # bitiş indexi
#result = result.group() # bulunan ifade gösterilir
#result = result.string # nerede arandığını gösterir



"""
    [] - köşeli parantez işlemleri
    
    köşeli parantez arasına yazılan tüm karakterler aranır

        [a-e] --- abcde
        [1-5] --- 12345
        [0-39] --- 01239
        
        [^abc] --- abc dışındaki karakterler
        [^0-9] --- rakam olmayan karakterler

"""
#result = re.findall("[0-9]",str)



"""
    . - herhangi bir tek karakteri belirtir
        
        .. --- iki karakter olan  eşleşir
               a  (not match)
               ab (1 match)
               abc (1 match)
               abcd (2 matches)
    
"""
#result = re.findall("...",str) üçlü gruplar oluşturur
#result = re.findall("Py..on",str) nokta yerine herhangi bir karakter gelebilir



"""
    ^ - belirtilen karakterle başlıyor mu ?
        
"""
#result = re.findall("^P",str) string in bütün hepsi içinde en baş




"""
    $ - belirtilen karakterle bitiyor mu?
    
"""
#result = re.findall("t$",str)
#result = re.findall("saat$",str)




"""
    * - bir karakterin sıfır ya da daha fazla sayıda olup olmadığını kontrol eder
        
        ma*n - mn : 1 match
               man : 1 match
               maaan : 1 match
               main : no match (a'nın arkasından n gelmiyor)
"""
#result = re.findall("sa*t",str) a karakterinden 0 veya daha fazla olması lazım




"""
    + - bir karakterin bir ya da faha fazla sayıda olmasını kontrol eder
        
        ma+n - mn : no match
               man  :1 match
               maaan : 1 match
               main : no match (a'nın arkasına n gelmiyor)
"""
#result = re.findall("sa+t",str)



"""
    ? - bir karakterin sıfır ya da bir kez tekrarladığını kontrol eder
        
        ma?n - mn : 1 match
               man : 1 match
               maaan : no match
               main : no match (a'nın arkasına n gelmiyor)
"""
#result = re.findall("sa?t",str)



"""
    {} - karakter sayısını kontrol eder
        
        al{2} : a karakterinin arkasına l karakteri 2 kez tekrarlanmalı
        al{2,5} : a karakterinin arkasına l karakteri en az 2 , en fazla 5 kez tekrarlanmalı
        [0-9]{2,4} : en az 2 en çok 4 basamaklı sayılar
        
"""
#result = re.findall("a{2}",str)



"""
    a|b - ya da anlamı vardır
        
        cde : no match
        ade : 1 match
        acdbea : 3 match
        
"""
#result = re.findall("P|K",str)



"""
    () - gruplama için kullanılır
    
        (a|b|c)xz : abc karakterlerinin arkasına xz gelmelidir
        
"""
#result = re.findall("(p|P)ython",str)



"""
    \ : özel karakterleri aramayı sağlar
    
        
    \A : belirtilen karakter string in başında mı?
        \Athe --- the string in başında mı
    
    \Z : belirtilen karakter string in sonunda mı ?
        the\Z --- the string in sonunda mı
    
    \b : belirtilen ifade kelimenin başında ya da sonunda mi?
        \bthe : kelimenin başında mi
        the\b : kelimenin sonunda mi
    
    \B : belirtilen ifade kelimenin başında ya da sonunda değil mi?
        \bthe : kelimenin başında değil mi
        the\b : kelimenin sonunda değil mi
    
    \s : boşluk karakteri
    \S : boşluk karakteri dışındakiler
    
    








"""
print(result)