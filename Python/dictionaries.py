# built-in data type data reperesent key-value pairs

# empty dictionay

emp_dict = {}

print(type(emp_dict))

# dictionary with key-value

my_dict = {"name":"Zulfiqar","age":27,"grade":"A"}

print(my_dict)

# using dict() constructor

person=dict(name = "Zulfiqar",age = 27,city="Naudero")
print(person)


mixed_dict = {"name":"Zulfiqar","grade":{"Maths":78,"english":96}}

print(mixed_dict)

# accesing items

print(person["name"])

print(mixed_dict.get("grade")) 

for key in person:
    print(f"{key}->{person[key]}")

for key,value in person.items():
    print(f"{key}:{value}")

# updating dictionary
    
person["grade"] = "B"

print(person)

# modify

person["age"] = 25

print(person)

# updating with other dictionary

new_person = {"coutry":"Pakistan","gender":"male"}

person.update(new_person)

print(person)

# deleting item

del person['gender']

print(person)

person.pop('age')
print(person)

person.clear()
print(person)