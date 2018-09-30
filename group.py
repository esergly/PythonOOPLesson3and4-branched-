import group_ex as gex

class Group:
    def __init__(self):
        self.group = []

    def search(self, surname):
        for element in self.group:
            if surname in element:
                print(element)
                return element
            else:
                print("This student is not found")
                return None

    def add(self, *person):
        try:
            if len(self.group) >= 10:
                raise gex.AddGroupException("The group is full!")
            else:
                self.group.append(person)
        except gex.AddGroupException as agerr:
            print(agerr.get_exception_message())
        return self.group

    def remove(self, surname):
        for i in range(len(self.group)):
            if surname == self.group[i][1]:
                del (self.group[i])
                return self.group[i]
            else:
                print("This student is not found")
                return 0

    def __str__(self):
        temp = ""
        for i in range(len(self.group)):
            for j in range(len(self.group[i])):
                temp += str(self.group[i][j]) + ', '
        return f"Group is: {temp}"

