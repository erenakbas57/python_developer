import json
import os

#TAMAMLANMADI VİDEOYU TEKRAR İZLE TAMAMLA

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load user from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users =json.load(file)

                for user in users:
                    user = json.loads(users)
                    print(user['username'])



    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("kullanıcı oluşturuldu")
    def login(self):
        pass
    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("users.json","w",encoding="utf-8") as file:
            json.dump(list,file)


repository = UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim = input("1- Kayıt ol\n2-Login\n3-Logout\n4-Kimlik\n5-Çıkış\nSeçiminiz : ")

    if secim=="5":
        break
    else:
        if secim =="1":
            username = input("username : ")
            password = input("password : ")
            email = input("email : ")

            user = User(username=username,password=password,email=email)
            repository.register(user)

            print(repository.users)
        elif secim == "2":
            pass
        elif secim == "3":
            pass
        elif secim == "4":
            exit()
        else:
            print("yanlış seçim")
            continue

