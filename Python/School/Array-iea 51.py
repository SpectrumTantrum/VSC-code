teachers = []

teachers.append("Mr Rees")
teachers.append("Mr l")
teachers.append("Miss Lomax")

print(teachers)

newTeacher = input("Enter a new teacher:")

teachers.append(newTeacher)

print(teachers)

teachers.remove("Mr Rees")

print(teachers)

print(teachers[0]," is the first teacher in the list!")
