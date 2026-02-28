student_marks = []

def input_students():
    repeat = True
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

def Students_display():
    print(student_marks)
    print('-'*79)
    print(f'| {'Student\'s name':<35} | {'quiz1':^5} | {'quiz2':^5} | {'quiz3':^5} | {'quiz4':^5} | {'Ave':^5} |')
    print('-'*81)

    for students in student_marks:
        total = 0 
        for i in range(1,5):
            total += students[i]
        average = total/4


        print(f'| {students[0]:<35}',end = ' | ')
        for i in range(1,5):   
            print(f'{students[i]:^5}',end = ' | ')
        print(f'{average:.2f} |')
    print('-'*81)

def highest_average():
    highest_avg = 0 
    top_student = ''
    for students in student_marks:
        total = 0 
        for i in range(1,5):
            total += students[i]
        avg = total/4

        if avg >highest_avg:
            highest_avg = avg
            top_student = students[0]


    print(f'\nStudent with highest average is {top_student} - {highest_avg:.2f}')

def highest_lowest_score():
    highest = student_marks[0][1]
    lowest = student_marks[0][1]

    for student in student_marks:
        for i in range(1, 5):
            if student[i] > highest:
                highest = student[i]
            if student[i] < lowest:
                lowest = student[i]

    print("Highest score overall:", highest)
    print("Lowest score overall:", lowest)

# Add new student
def add_student():
    name = input("Enter new student name: ")
    new_student = [name]

    for i in range(1, 5):
        score = int(input(f"Enter score for Quiz {i}: "))
        new_student.append(score)

    student_marks.append(new_student)
    print("Student added successfully!")

# Update student score
def update_score():
    name = input("Enter student name to update: ")

    for student in student_marks:
        if student[0].lower() == name.lower():
            quiz_number = int(input("Enter quiz number (1-4): "))
            new_score = int(input("Enter new score: "))
            student[quiz_number] = new_score
            print("Score updated successfully!")

    print("Student not found.")








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

    
    if choice == "1":
        input_students()
    elif choice == "2":
        Students_display()
    elif choice == "3":
        highest_average()
    elif choice == "4":
        highest_lowest_score()
    elif choice == "5":
        add_student()
    elif choice == "6":
        update_score()
    elif choice == "7":
        break
    else:
        print("Invalid choice.")