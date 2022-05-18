from human import Human


class Student(Human):

    def __init__(self, name, last_name, age, speciality, course, group_number):
        super().__init__(name, last_name, age)
        self.speciality = speciality
        self.course = course
        self.group_number = group_number

    def __str__(self):
        return 'Student [' + super().__str__() + ', speciality = {}, course = {}, group_number = {}]'.format(
            self.speciality, self.course, self.group_number)
