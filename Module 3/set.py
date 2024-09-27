# set: unique items collenction
# set --> {}
# tuplw --> ()
# list --> []
numbers = [12,34,5,78,657,756,45]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(25)
print(numbers_set)
numbers_set.remove(45)
print(numbers_set)

A ={1,3,5,7}
B ={1,5,7,9}
print(A & B)   # A intersection B
print(A | B)   # A Union B