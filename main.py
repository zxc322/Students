# Подразумевается что все файлы лежат в одной директории

from human import Human
from student import Student
from group import Group

human1 = Human('Artur', 'Johnson', 32)
print(human1)
student1 = Student('Cristiano', 'Ronaldo', 32, 'GO', 2, 4)
print(student1)
group1 = Group()
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
group1.add_student(student1)
print('#' * 30)
print(group1)

