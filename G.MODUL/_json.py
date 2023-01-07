import json

#person_string = '{"name":"Eren","surname":"Akbaş"}'

# JSON string to Dictionary
"""
result = json.loads(person_string)
result1 = result["name"]

print(type(result)) # DİCTİONARY
print(result)
print(result1)

#DOSYADAN ÇEKİLEN VERİ
with open("person.json") as f:
    data = json.load(f)
    print(data["surname"])

"""

# Dictionary to JSON string

person_dict = {
    "name" : "ali",
    "surname" : "erbaş"
}

#result = json.dumps(person_dict)
#print(result["name"])   yazdırılmaz artık string oldu
#print(type(result))

# DOSYAYA AKTARILAN VERİ
with open("person.json","w") as f:
    json.dump(person_dict,f)