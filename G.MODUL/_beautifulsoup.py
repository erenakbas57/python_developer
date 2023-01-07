from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Eren Akbaş</title>

</head>
<body>

    <h1 id="header">
Python Kursu
</h1>

    <div class="grup1">
<h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
            <li>Menü 4</li>
            <li>Menü 5</li>
        </ul>
</div>


     <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>


</body>
</html>
"""

soup = BeautifulSoup(html_doc ,"html.parser")

result = soup.prettify() # prettify dökumanı düzenleme işlemi yapıyor

#etiketleri almayı sağlayan kod
result1 = soup.title         #title hepsini alır içerikle beraber
result1 = soup.title.name    # tek title ismini alır
result1 =soup.head.string    # title içindeki kısımları alır


result2 = soup.find_all("h2") # h2 olanlar gelir liste şeklinde

#div içindeki ul içindeki li ler
result2 = soup.find_all("div")[1].ul.find_all("li")
result2 = soup.find_all("div")[1].ul.li # böyle sadece ilk li etiketi gelir

result3 = soup.div.findChildren() # div in altındaki tüm elemanlar gelir

result3 = soup.div.findNextSibling() # bir sonraki div gelir

print(result3)