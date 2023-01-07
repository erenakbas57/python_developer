# class :

class Person:
    pass # yer tutucu. normalde boş olduğu için hata verirdi. şimdi cermiyor. ama hiçbir şeyde yapmıyor

    # class attribute
    address = 'no information'

    #constructor(yapıcı metodlar)
    ## yapıcı metodlar çağırılmadan direk obje üzerinden çalışırlar
    def __init__(self,name,year):
        #object attributes
        self.name = name
        self.year = year
        print("init methodu çalıştı")

    #methods

#object (instance)
p1 = Person('eren',2001)

#updating
p1.name = 'Melike'

#accessing object attributes
print(f"name : {p1.name} . year : {p1.year} . address : {p1.address}")
