class Student:
    def __init__(self,name,cur_class,id):
        self.name = name
        self.cur_class = cur_class
        self.id=id

    def __repr__(self) -> str:
        return f'Student name: {self.name} , student class: {self.cur_class} and student id: {self.id}'
    
class Teacher:
    def __init__(self,t_name,t_sub,t_id) -> None:
        self.t_name=t_name
        self.t_sub=t_sub
        self.t_id=t_id

    def __repr__(self) -> str:
        return f'Teacher name: {self.t_name} , teacher subject: {self.t_sub} and teacher id: {self.t_id}'
    
class School:
    def __init__(self,name) ->None:
        self.name=name
        self.teachers=[]
        self.students=[]

    def add_teacher(self,name,subject):
        id=len(self.teachers) + 200
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student=Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}'

    def __repr__(self):
        print('Welcome to', self.name)
        print('-------Our Teachers----------')
        for teacher in self.teachers:
            print(teacher)
        print('----------Our Students--------')
        for stu in self.students:
            print(stu)
        return 'All done for now'


# alia = Student("Alia vat",8,42)
# ranvir =Teacher("Ranvir",'DSA',345)
# print(alia)

phtron = School('Phitron')
phtron.enroll('alia',49499)
phtron.enroll('ali',4999)
phtron.enroll('aia',499)
phtron.enroll('lia',4949)
phtron.add_teacher("Rifat",'DSA')

print(phtron)
