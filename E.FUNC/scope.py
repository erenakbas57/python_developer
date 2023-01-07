
name = "global scope" # eren de olmasaydı global scope yazacaktı

def greeting():
    name ='eren' # melike olmasaydı eren yazacaktı

    def hello():
        name ='melike' # bu durumda melike yazar.
        print(name)
    hello()

#greeting()
#print(name)

########################################################3

x=50
def test(x):
    print(f'x : {x}')

    x=100
    print(f'changed x to {x}')

test(x)
print(x) # x=50 : x global de 100 değerini almadı func içinde 100 değerini aldı

# func içinden global değişkenin değerini degiştirmek için global kullanırız

y=10
def test2():
    global y
    print(f'y : {y}')

    y=25
    print(f'changed y to {y}')

test2()
print(y) # y=25 globalde de değeri değişmiş oldu