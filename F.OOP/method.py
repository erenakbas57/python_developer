
class person:
    # class attribute
    address = 'no information'

    # constructor(yapıcı metodlar)
    # yapıcı metodlar çağırılmadan direk obje üzerinden çalışırlar
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year




    #method
    def intro(self):
        print("Hello World")

    def calculateAge(self):
         return 2021-self.year



p1 = person('Eren',2001)
print(p1.address)


class circle:
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = circle() # yaricap = 1
c2 = circle(5)

print(f"c1 alan : {c1.alan_hesapla()} \nc1 çevre : {c1.cevre_hesapla()} ")
print(f"c2 alan : {c2.alan_hesapla()} \nc2 çevre : {c2.cevre_hesapla()} ")