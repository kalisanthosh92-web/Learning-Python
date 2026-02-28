repeat = True
students = 1
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
    if repeat == 'yes':
        repeat = True
    else :
        repeat = False
    students += 1

print(student_marks)
print('-'*100)

sum = 0 
for row in student_marks:
    for col in range(1,5):
        sum += student_marks[row][col]



