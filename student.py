import man


class Student(man.Man):
    def __init__(self, name, surname, sex, growth, weight, university, faculty, group):
        super().__init__(name, surname, sex, growth, weight)
        self.university = university
        self.faculty = faculty
        self.group = group

    def __str__(self):
        return "Student: " + super().__str__() + "university = {}, faculty = {}".format(self.university,
                                                                                        self.faculty)
