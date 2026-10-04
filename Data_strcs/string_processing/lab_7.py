student_records = [
    ["Allen", 85],
    ["Bob", 90],
    ["Charles", 78],
    ["Xavier", 88],
    ["Eren", 92]
]


#part A
def count_students(records):
    if bool(records) == False:
        return 0
    return 1 + count_students(records[1:])


def calculate_total(records):
    if bool(records) == False:
        return 0
    current_mark = records[0][1]
    return current_mark + calculate_total(records[1:])

def calculate_average(records):
    total_students = count_students(records)
    if total_students == 0:
        return 0
    return calculate_total(records) / total_students


def find_highest(records):
    if bool(records) == False:
        return 0
    highest = records[0][1]
    marks = find_highest(records[1:])
    if highest < marks:
        return marks
    return highest

def search_student(records, name):
    if bool(records) == False:
        print('Student not found.')
        return None
    student = records[0]
    if student[0].lower() == name.lower():
        print("Student Found!")
        print(f'Name: {student[0]}')
        print(f"Grades: {student[1]}")
        return student
    return search_student(records[1:], name)

def display_records(records):
    if bool(records) == False:
        return None
    student = records[0]
    print(f"{student[0]}: {student[1]}")
    display_records(records[1:])


def count_passed(records):
    if bool(records) == False:
        return 0
    if records[0][1] >= 75:
        is_passed = 1 
    else :
        is_passed = 0
    return is_passed + count_passed(records[1:])


def count_failed(records):
    if bool(records) == False:
        return 0
    if records[0][1] < 75:
        is_failed = 1 
    else :
        is_failed = 0
    return is_failed + count_failed(records[1:])



def main():
    while True:
        print()
        print("=======================================")
        print("    RECURSIVE STUDENT RECORD SYSTEM    ")
        print("=======================================")
        print("1. Display Student Records")
        print("2. Count Students")
        print("3. Calculate Total Marks")
        print("4. Calculate Average Mark")
        print("5. Find Highest Mark")
        print("6. Search Student")
        print("7. View Pass/Fail Statistics")
        print("8. Exit")
        print("=======================================")
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            print("\n--- Student Records ---")
            display_records(student_records)
        elif choice == '2':
            print(f"\nTotal Students: {count_students(student_records)}")
        elif choice == '3':
            print(f"\nTotal Marks: {calculate_total(student_records)}")
        elif choice == '4':
            print(f"\nAverage Mark: {calculate_average(student_records):.2f}")
        elif choice == '5':
            high = find_highest(student_records)
            print(f"\nHighest Mark: {high}")
        elif choice == '6':
            name_to_search = input("\nEnter student name to search: ")
            search_student(student_records, name_to_search)
        elif choice == '7':
            print(f"\nNumber of Students Passed: {count_passed(student_records)}")
            print(f"Number of Students Failed: {count_failed(student_records)}")
        elif choice == '8':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()
