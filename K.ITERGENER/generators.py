# generators : bellekte yer kaplamayan iterator üretiyor

def cube():
    for i in range(5):
        yield i**3
#ya da

liste = (i**3 for i in range(5))

for i in liste:
    print(i)

for i in cube():
    print(i)

# ne zaman istersek yield o kadar çalıştırılır.
# bir kere print yaparsak yield for döngüsü içinde olsa da
#bir kere çalışır.