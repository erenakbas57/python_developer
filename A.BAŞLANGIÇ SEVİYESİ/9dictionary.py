#       plakalar = {"key":"value"}

plakalar = {1:"adana",34:"istanbul",43:"kütahya",57:"sinop"}
print(plakalar[1])   # adana bilgisini döndü

plakalar[6]  = "ankara"    # eleman ekleme
print(plakalar)

plakalar[6] = "ANKARA"   # güncelleme işlemi

# iç içe key value değerleri atanabilir

user = {
    'eren' : {
        'age' : 36,
        'job' :'student',
        'roles': ['admin','user']
    },
    'omer' : {
        'age' :34,
        'job' :'student',
        'roles' : ['user']
    }
}

print(user['eren']['roles'])