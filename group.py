from exception import GroupIsFull


class Group:

    def __init__(self):
        self.students_list = []

    def add_student(self, new_student):
        try:
            if len(self.students_list) < 10:
                self.students_list.append(new_student)
            else:
                raise GroupIsFull()
        except GroupIsFull as err:
            print(err)

    def remove_student(self, student):
        self.students_list.remove(student)

    def search(self, last_name):
        for i in self.students_list:
            if last_name == i.last_name:
                res = i
                break
            else:
                res = 'Student with last name <' + last_name + '> not in group.'
        return res

    def converter(self):  #
        res = ''
        for i in self.students_list:
            i = str(i)
            res += i
            res += '\n'
        return res

    def __str__(self):
        return Group.converter(self)
