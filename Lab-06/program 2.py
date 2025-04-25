students = [(101, "Alice", 20), (102, "Bob", 21), (103, "Charlie", 22)]

roll_nos = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)
