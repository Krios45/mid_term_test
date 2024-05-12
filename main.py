from StudentManagement import QLSV

def main():
    print("Welcome to the student management program!!... (^_^)")
    print("-----------------------------------------------")
    print("1. Add student.")
    print("2. Show student.")
    print("3. Delete student.")
    print("4. Exit.")
    print("-----------------------------------------------")
    list_student = []
    while True:
        choice = int(input("Enter your option: "))
        if choice == 1:
            student = QLSV()
            list_student = student.add_student()
            print("-----------------------------------------------")
        elif choice == 2:
            if not list_student:
                print("No student to show!!... (0_0!)")
                continue
            else:
                student = QLSV()
                student.show_student(list_student)
                print("-----------------------------------------------")    
        elif choice == 3:
            if not list_student:
                print("No student to delete!!... (0_0!)")
            else:
                student = QLSV()
                student.delete_student(list_student)
                print("-----------------------------------------------")
        elif choice == 4:
            student = QLSV()
            student.exit() 
        else:
            print("Invalid option!!... (-_-!)")
            print("-----------------------------------------------")

main()

    