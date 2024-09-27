def full_name(first,last):
    name =f'Full name is: {first} {last}'
    return name

# take parameters in order( serial wise)
# name = full_name("MD","Rifat")

name = full_name(last="Rifat",first="MD")
print(name)

# kargs

def famous_name(first,last,**aditional):
    name=f'{first} {last}'
    # print(aditional)
    # print(aditional['tital'])
    for key,value in aditional.items():
        print(key,value)
    return name
name = famous_name(first="MD",last="Rifat",tital="Software Enginner",works="Make money")
print(name)