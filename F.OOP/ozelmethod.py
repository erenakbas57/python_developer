#Special method

myList = [1,2,3]
myString = "Eren Akbaş"

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))

class Movie():
    def __init__(self, director, title, duration):
        self.director = director
        self.title = title
        self.duration = duration
        print("Movie objesi oluşturuldu")

m = Movie("David Fincher", "Fight Club" , "2 saat")
print(m)
