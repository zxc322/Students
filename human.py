class Human:

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return 'name = {}, last_name = {}, age = {}'.format(self.name, self.last_name, self.age)
