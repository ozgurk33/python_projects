class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

class School:
    def __init__(self):
        self.students = []

    def add_students(self, name, age, roll_number):
        student = Student(name,age,roll_number)
        self.students.append(student)
    
    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Roll Number: {student.roll_number}")
            print("----------------------------------------------")
    
    def edit_student(self, roll_number, new_name, new_age):
        for student in self.students:
            if student.roll_number == roll_number:
                student.name = new_name
                student.age = new_age
                print(f"Student {student.name} successfully updated.")
                return
    
    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student {student.name} deleted successfully")
                return


#creating school object
school = School()

while True:
    choice = input("Enter your choice: \n1) Add Student \n2) Display list of students"
                   "\n3) Edit student data \n4) Remove Student \n5) Quit\n")
    if choice == "1":
        #accepting data from the user to create a student object
        name = input("Enter name of the student: ")
        age = input("Enter age: ")
        roll_number = input("Enter roll number: ")

        #creating a student object and adding it to the student list 
        school.add_students(name, age, roll_number)
    
    elif choice == "2":
        school.display_students()

    elif choice == "3":
        roll_number = input("Enter roll number which you want to edit: ")
        new_name = input("Enter new name for the student: ")
        new_age = input("Enter new age for the student: ")
        school.edit_student(roll_number, new_name, new_age)

    elif choice == "4":
        roll_number = input("Enter roll number you want to delete: ")
        school.delete_student(roll_number)

    elif choice == "5":
        break
