students = ["John", "Sarah", "Mike", "John"]
students.append("Patrick")
# print(students)
# students[0] = "Simon"
# print(students)
students.remove("Mike")
# print(students)
# print("John" in students)
print(students.index("Sarah"))
sarah_pos = students.index("Sarah")
students[sarah_pos] = "Mary"
print(students)
print(students.count("John"))