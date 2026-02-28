while True:
    print("\n--- Student Grade Management System ---")
    print("1. To enter Students Details")
    print("2. Display Students")
    print("3. Show Highest Average")
    print("4. Show Highest and Lowest Score")
    print("5. Add Student")
    print("6. Update Score")
    print("7. Exit")

    choice = input("Enter choice: ")

repeat = True
student_marks = []
while repeat:
    name = input('Enter name of the student,')
    quiz1 = int(input('Enter the score of quiz 1:'))
    quiz2 = int(input('Enter the score of quiz 2:'))
    quiz3 = int(input('Enter the score of quiz 3:'))
    quiz4 = int(input('Enter the score of quiz 4:'))
    repeat = input('Do u have more students data to input? (yes/no)').lower()
    record = [name,quiz1,quiz2,quiz3,quiz4]
    student_marks.append(record)
    if repeat == 'y' or repeat == 'Y':
        repeat = True
    else :
        repeat = False






    if choice == "1":
        display_students()
    elif choice == "2":
        highest_average()
    elif choice == "3":
        highest_lowest_score()
    elif choice == "4":
        add_student()
    elif choice == "5":
        update_score()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")