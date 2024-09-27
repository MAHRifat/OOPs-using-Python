# function is a first class object
def double_decker():
    print('Staring the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun

# print(double_decker())
print(double_decker()())

def do_something(word):
    print('Start work')
    word()
    print('end work')

def coding():
    print('coding in python')

do_something(coding)