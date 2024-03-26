#Klass för elev
class student:
    def __init__(self, f_name : str, l_name : str, age : int, gender : str):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f"{self.f_name} {self.l_name} {self.age} {self.gender}"

#Klass för lärare
class teacher:
    def __init__(self, f_name : str, l_name : str, age : int, gender : str):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f"{self.f_name} {self.l_name} {self.age} {self.gender}"

#Klass för elev, lärare och ämne
class group:
    def __init__(self, subject : str, teacher : teacher, students : list):
        self.subject = subject
        self.teacher = teacher
        self.students = students
    
    def __str__(self):
        students_string = ""

        for student in self.students:
            students_string += student.f_name + " "

        return f"{self.subject} {self.teacher} {students_string}"

    def add_student(self, new_student):
        self.students.append(new_student)

melvin = student("Melvin", "Lindholm", 17, "Male")
mattias = teacher("Mattias", "Leijon", 52, "Male")
program = group("Programmering", mattias, [melvin])

program.add_student(melvin)
print(program)