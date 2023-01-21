import pandas as pd

df = pd.read_csv("zimdbdemo.csv")

# 1- Dosyada hakkındaki bilgiler
result = df

# 2- İlk 5 kaydı göster
result = df.head()

# 3- ilk 10 kaydı göster
result = df.head(10)

# 4- son 5 kaydı göster
result = df.tail()

# 5- son 10 kaydı göster
result = df.tail(10)

# 6- Sadece Title kolonunu al
result = df["Title"]

# 7- Sadece Title kolonunu içeren ilk 5 kaydı al
result = df["Title"].head()

# 9- Sadece Title ve Rating kolonunu içeren son 7 kaydı al
result = df[["Title","imdbRating"]].tail(7)

# 10- Sadece Title ve Rating kolonunu içeren 2. 5 kaydı al
result = df[5:][["Title","imdbRating"]].head()

# 11- Sadece Title ve Rating kolonunu içeren ve imdbRAting i 8.0 üstü
#     olan kayıtlardan ilk 50 tanesi al
result = df[df["imdbRating"] >=8.0][["Title","imdbRating"]].head(50)

# 12- Yayın tarihi 1970-2000 arasımda olan filmlerin isim listesi
result = df[(df["Year"] >2005) & (df["Year"] <2015)]["Title"]

# 13- imdb puanı 8-9 arasında olan ya da dili türkçe olan filmleri getirin
result = df[((df["imdbRating"]<=9) & (df["imdbRating"] >=8)) | (df["Language"] == "Turkish")]["Title"]

