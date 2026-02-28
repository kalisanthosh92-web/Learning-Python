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
    print(f'{average:.2f}')




print('-'*81)














#sum = 0 
#for row in student_marks:
 #   for col in range(1,5):
  #      sum += row[col]





