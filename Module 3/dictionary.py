# key value pair
# dictionary
# object
# hash table
# overlap with set

person ={'name': 'Rifat','address': 'Comilla','Age': 23 , 'job': 'Bekar'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language']='python'

print(person)

person['name'] = 'Other'
print(person)

del person['Age']
print(person)

for k,v in person.items():
    print(k,v)
