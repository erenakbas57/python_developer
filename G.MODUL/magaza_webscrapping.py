import requests
from bs4 import BeautifulSoup

url = "https://www.epey.com/akilli-telefonlar/e/Tjtfczo5OiJwdWFuOkRFU0MiOw==/"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("ul",{"class":"metin row"},limit=1)

print(list)
for ul in list:
    name = ul.li.find("div",{"class":"detay cell"}).find("a",{"class":"urunadi"}).title
    print(name)
