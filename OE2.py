full_name = input('Enter fullname: ').strip()
course_code = input('Enter course code: ').upper().strip()
year_level = int(input('Enter year level(1-4): '))
DOB = input('Enter date of birth (MM/DD/YYYY): ')

if len(full_name ) < 2:
    print('Enter a valid name!')
last_name = full_name.split()[-1]
if year_level > 4 or year_level<1:
    print('Enter valid year level!')

DOB_valid = True 
dob_lst = DOB.split('/')

day = int(dob_lst[1])
month =int(dob_lst[0])
year = int(dob_lst[2])

if month in range(1,13):
    if month == 2 and  day in range(1,30):
        if year%4 == 0  or year%100 ==0 :
            DOB_valid = True 
        else:
            print('invalid birth date!')
            DOB_valid = False
    else:
        if month//2 == 1:
            if day in range(1,32):
                DOB_valid = True 
            else:
                print('invalid birth date!')
                DOB_valid = False
        else :
            if day in range(1,31):
                DOB_valid = True
            else:
                print('invalid birth date!')
                DOB_valid = False
else : 
    DOB_valid = False

student_id = course_code+'-'+str(year_level)+'-'+last_name.upper()+'-'+str(year)

print(student_id)
#print(DOB_valid)

width = 50
print('='*50)
print(f'|{'STUDENT ID CARD':^48}|')
print('='*50)
print(f'| {'Name':<12}:{full_name:<33} |')
print(f'| {'Course':<12}:{course_code:<33} |')
print(f'| {'Year':<12}:{year_level:<33} |')
print(f'|{' '*48}|')
print(f'| {'Student ID':<12}:{student_id:<33} |')
print('='*50)
