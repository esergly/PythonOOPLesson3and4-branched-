import man
import group as gr
import student

# Create man
person = man.Man("John", "Maldivian", "Male", 178, 69)
print(person)
# Create student
student_test = student.Student("Jason", "Winn", "Male", 174, 81, "Oxford", "Politics", "P3")
print(student_test)
# Create group
group = gr.Group()
group.add("John", "Silver", "Male", 185, 85, "Michigan", "Economics", "E4")
group.add("Liz", "Taylor", "Female", 167, 45, "Stanford", "Article", "A2")
group.add("Kate", "Milton", "Female", 172, 55, "San-Diego", "IT", "I1")
group.add("Bob", "Norton", "Male", 180, 73, "Stanford", "Article", "A4")
group.add("Serg", "Ginzburg", "Male", 173, 65, "San-Diego", "IT", "I2")
group.add("Kent", "Baldwin", "Male", 178, 75, "Michigan", "Economics", "E5")
group.add("Jack", "Nicholson", "Male", 167, 80, "Stanford", "Article", "A5")
group.add("Paul", "Robinson", "Male", 165, 58, "San-Diego", "IT", "I2")
group.add("Christine", "Ye", "Female", 160, 40, "San-Diego", "IT", "A3")
group.add("Diana", "Kimble", "Female", 159, 45, "Stanford", "Article", "A1")
print(group)
# UserException test
group.add("Test", "Test", "Test", 100, 100, "Test", "Test", "Test")
group.add("Test", "Test", "Test", 100, 100, "Test", "Test", "Test")
group.add("Test", "Test", "Test", 100, 100, "Test", "Test", "Test")
# Search and remove functions
group.search("Winn")
group.search("Silver")
group.remove("Silver")
print(group)
