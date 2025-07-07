


# student management system project using python

print("******* STUDENT MANAGEMENT SYSTEM PROJECT *******")

def student_management(students_data):
    print("choose the operation you want to perform:\n",
          "1.Student List:\n",
          "2.Add student to List:\n",
          "3.Remove student from List:\n",
          "4.Search student Data:\n")


    try:
      choice = int(input("enter your choice:"))
      if choice >= 1 and choice <= 4:
        if choice == 1:
          if not students_data:
            print("student list is empty")
          else:
            print("student list:")
            for name, details in students_data.items():
                print(f"Name: {name}")
                for key, value in details.items():
                    print(f"  {key.replace('_', ' ').title()}: {value}")
        elif choice == 2:
          print("Add student Details:")
          name = input("student name:")
          age = int(input("student age:"))
          student_class = input("student class:")
          roll_number = int(input("student roll number:"))
          students_data[name] = {"age": age, "student_class": student_class, "roll_number": roll_number} # Use students_data
          print("student added successfully")
        elif choice==3:
          print("Remove student Details:")
          name=input("Enter student name:")
          if name in students_data:
            del students_data[name]
            print("student removed successfully")
          else:
            print("student not found")
        elif choice==4:
          name=input("Enter student name:")
          if name in students_data:
            print("student details:")
            details = students_data[name]
            print(f"Name: {name}")
            for key, value in details.items():
                print(f"  {key.replace('_', ' ').title()}: {value}")
          else:
            print("student not found")
      else:
        print("Invalid number ,Try Again!!!")
    except ValueError:
      print("ValueError, Please enter valid choice")

students_data = {}
while True:
    student_management(students_data)
    print("\nIf you want to try again")
    print("Enter Y to try again")
    print("Enter N to Stop")

    choose = input("Enter Y/N:").upper()
    if choose == 'Y':
        continue
    elif choose == 'N':
        print("Thank you for using student management system")
        break
    else:
        print("Invalid input. Please enter Y or N.")