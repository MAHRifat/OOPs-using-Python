# lambda

def double(x):
    return 2*x
print(double(4))


doubled = lambda num : num * 2
print(doubled(4))

numbers =[22,3,4,23,23,224,24,24,23]
doubled_nums=map(doubled,numbers)
squre_nums=map(lambda x: x*x,numbers)
print(list(doubled_nums))
print(list(squre_nums))


actors = [
    {'name': 'sabana','age': 65},
    {'name': 'saban','age': 45},
    {'name': 'saba','age': 35},
    {'name': 'sab','age': 30},
    {'name': 'sa','age': 38}
]

juniors = filter(lambda actor : actor['age']<40 , actors)
print(list(juniors))