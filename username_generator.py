full_name = input('Enter your full name: ')
birth_year = int(input('Enter your birth year: '))


#print(full_name.strip().lower()[0:3])

name_valid = full_name.strip().split(' ')
if len(name_valid) >= 2:
    name1 = name_valid[0].lower()[0:3]
    name2 = name_valid[len(name_valid) - 1 ].lower()[0:3]
    name3 = str(birth_year)[-1:-3:-1]
else:
    print('The name doesnot have a last name!')

user_name = name1+name2+name3
print(f" '{full_name}' + {birth_year} ->  '{user_name}' ")
    