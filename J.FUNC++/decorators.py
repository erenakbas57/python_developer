# decorators fonksiyonları , fonksiyonlara özellik eklemek için kullanırız

def my_decorator(func):
    def wrapper():
        print("fonksiyondan önce işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator
def sayHello(name):
    print("hello")

def my_decorator2(func):
    def wrapper(name):
        print("fonksiyondan önce işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator2
def sayName(name):
    print("greeting", name)

#name bilgisi yollayabilmek için wrapper a ve
#içindeki func a da name parametresi yolladık


# sayGreeting = my_decorator(sayName)

#bu işlem yerine decorator ile daha kolay yapabiliriz.

#sayName("Eren")

#**********************************************************

import math
import time

def calculate_time(func):
    def inner(*args):
        start = time.time()
        time.sleep(1)
        func(*args)
        finish = time.time()
        print(f"{func.__name__} fonksiyonu {finish - start} saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    #time.sleep(3)  uygulamayı uyutma işlemi
    print(int(math.pow(a,b)))
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))


usalma(2,3)
faktoriyel(5)