# inheritance (kalıtım) : miras alma

class Person():
    def __init__(self, fname , lname):
        self.firstname = fname
        self.lastname = lname
        print("Person created...")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        self.StudentNumber = number
        print("Student Created")
        # bu durumda bu init person initi ezer ve sadece bu çalışır student için

        # ama bunu yazarsak person init de çalışır
        Person.__init__(self, fname, lname)

    #override
    def who_am_i(self):
        print("I am a student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        #person init i çalıştırmak için başka yöntem
        super().__init__(fname, lname)
        self.branch = branch # sağfaki branch dışarıdan gelen değerdir

    def who_am_i(self):
        print("I am a teacher")


p1 = Person('Muharrem','Akbaş')
s1 = Student('Eren','Akbaş', 384)

print(f"adı : {s1.firstname}  \nsoyadı : {s1.lastname}")

s1.who_am_i()
p1.who_am_i()
s1.eat()