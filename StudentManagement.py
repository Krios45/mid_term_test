import json

class Student:

    __name = str 
    __age = int    
    __gender = str
    __id = int
    __email = str
    __address = str
    __major = str # Chuyên ngành

    def __init__(self, name='', id=0, age=0, gender='', email='', address='', major=''):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__id = id
        self.__email = email
        self.__address = address
        self.__major = major
    
    def __str__(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nGender: {self.__gender}\nID: {self.__id}\nMajor: {self.__major}\nEmail: {self.__email}\nAddress: {self.__address}"

    def get_id(self):
        return self.__id
    
    def add_student(self):
        self.__name = str(input("Enter name: "))
        self.__age = int(input("Enter age: "))
        self.__gender = str(input("Enter gender: "))
        self.__id = int(input("Enter ID: "))
        self.__email = str(input("Enter email: "))
        self.__address = str(input("Enter address: "))
        self.__major = str(input("Enter major: "))

class FirstYear(Student):

    __school = str # Trường cấp 3 theo học
    __point = float # Điểm thi THPT

    def __init__(self, name='', id='', age='', gender='', email='', address='', major='', school='', point=''):
        super().__init__(name, id, age, gender, email, address, major)
        self.__school = school
        self.__point = point

    def __str__(self):
        return super().__str__() + f"\nSchool: {self.__school}\nPoint: {self.__point}"
    
    def add_student(self):
        super().add_student()
        self.__school = str(input("Enter school: "))
        self.__point = float(input("Enter point: "))

class SecondYear(Student):

    __gpa = float
    __scholarship = str

    def __init__(self, name='', id='', age='', gender='', email='', address='', major='', gpa='', scholarship=''):
        super().__init__(name, id, age, gender, email, address, major)
        self.__gpa = gpa
        self.__scholarship = scholarship

    def __str__(self):
        return super().__str__() + f"\nGPA: {self.__gpa}\nScholarship: {self.__scholarship}"
    
    def add_student(self):
        super().add_student()
        self.__gpa = float(input("Enter GPA: "))
        self.__scholarship = str(input("Enter scholarship: "))

class ThirdYear(Student):

    __gpa = float
    __scholarship = str
    __company = str # Công ty thực tập

    def __init__(self, name='', id='', age='', gender='', email='', address='', major='', gpa='', scholarship='', company=''):
        super().__init__(name, id, age, gender, email, address, major)
        self.__gpa = gpa
        self.__scholarship = scholarship
        self.__company = company

    def __str__(self):
        return super().__str__() + f"\nGPA: {self.__gpa}\nScholarship: {self.__scholarship}\nCompany: {self.__company}"

    def add_student(self):
        super().add_student()
        self.__gpa = float(input("Enter GPA: "))
        self.__scholarship = str(input("Enter scholarship: "))
        self.__company = str(input("Enter company: "))
        
class FourthYear(Student):

    __gpa = float
    __scholarship = str
    __company = str
    __project = str # Đề tài nghiên cứu

    def __init__(self, name='', id='', age='', gender='', email='', address='', major='', gpa='', scholarship='', company='', project=''):
        super().__init__(name, id, age, gender, email, address, major)
        self.__gpa = gpa
        self.__scholarship = scholarship
        self.__company = company
        self.__project = project
    
    def __str__(self):
        return super().__str__() + f"\nGPA: {self.__gpa}\nScholarship: {self.__scholarship}\nCompany: {self.__company}\nProject: {self.__project}"

    def add_student(self):
        super().add_student()
        self.__gpa = float(input("Enter GPA: "))
        self.__scholarship = str(input("Enter scholarship: "))
        self.__company = str(input("Enter company: "))
        self.__project = str(input("Enter project: "))

list_student = []
class QLSV:

    def add_student(self):
        n = int(input("Enter number of student: "))
        if not n>0:
            raise ValueError("Number of student must higher than 0!!... (-_-!)")     
        for i in range(n):
            print("Student:", i+1)
            print("1. First year student")
            print("2. Second year student")
            print("3. Third year student")
            print("4. Fourth year student")
            try:
                print("---------------------------------")
                choice = int(input("Enter your choice: "))                            
                if choice == 1:
                    student = FirstYear()
                    student.add_student()
                    list_student.append(student)
                elif choice == 2:
                    student = SecondYear()
                    student.add_student()
                    list_student.append(student)
                elif choice == 3:
                    student = ThirdYear()
                    student.add_student()
                    list_student.append(student)
                elif choice == 4:
                    student = FourthYear()
                    student.add_student()
                    list_student.append(student)            
            except ValueError:
                print("Only integer number!!... (-_-!)")
        return list_student
    
    # Serialize (Tuần tự hoá) - Dùng để lưu sinh viên vào file json
        json_string = json.dumps([student.__dict__ for student in list_student], indent=4)
        print(json_string)
        with open("list_student.json", "w") as file:
            file.write(json_string)

    # Deserialize (Khôi hồi) - Dùng để đọc dữ liệu sinh viên từ file json
        with open("list_student.json", "r") as file:
            data = json.load(file)
            print(data)

    def show_student(self, list_student):
        
        # Divide student into each year
        first_year_student = [student for student in list_student if isinstance(student, FirstYear)]
        second_year_student = [student for student in list_student if isinstance(student, SecondYear)]
        third_year_student = [student for student in list_student if isinstance(student, ThirdYear)]
        fourth_year_student = [student for student in list_student if isinstance(student, FourthYear)]
        
        # Show first year student
        print("First year student:")
        if not first_year_student:
            print("No student!!... (0_0!)")
            print("---------------------------------")
        for student in first_year_student:
            print(student)
            print("---------------------------------")

        # Show second year student
        print("Second year student:")
        if not second_year_student:
            print("No student!!... (0_0!)")
            print("---------------------------------")
        for student in second_year_student:
            print(student)
            print("---------------------------------")
        
        # Show third year student
        print("Third year student:")
        if not third_year_student:
            print("No student!!... (0_0!)")
            print("---------------------------------")
        for student in third_year_student:
            print(student)
            print("---------------------------------")

        # Show fourth year student
        print("Fourth year student:")
        if not fourth_year_student:
            print("No student!!... (0_0!)")
        for student in fourth_year_student:
            print(student)
            
    def delete_student(self, list_student):
        n = int(input("Enter ID to delete student: "))
        found = False
        for student in list_student:
            if student.get_id() == n:
                list_student.remove(student)
                print("Delete student successfully!!... (^_^)")
                found = True
                break
        if not found:
            print("Can't find student!!... (-_-!)")

    def exit(self):
        print("Goodbye!!... <3")
        exit()


                    
            



    
    
