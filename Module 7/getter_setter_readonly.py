class User:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money
#   getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age
    @property
    def salary(self):
        return self.__money
    
#   setter
    @salary.setter
    def salary(self,value):
        if value < 0:
            print('salary can\'t be negative')
        self.__money+=value


    
sumsu = User('Kopa',25,13434)
# print(sumsu.__money) # give us error because the money is private
(sumsu.age)  #call method bt like attribute
# print(sumsu.salary())
print(sumsu.salary)

sumsu.salary=4000
print(sumsu.salary)