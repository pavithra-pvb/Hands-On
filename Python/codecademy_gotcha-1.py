def createStudent(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades
    }

chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

def addGrade(student, grade):
    student['grades'].append(grade)
    print(student['grades'])

addGrade(chrisley, 90)
addGrade(dallas, 100)
