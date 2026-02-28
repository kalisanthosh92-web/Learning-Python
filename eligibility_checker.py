age = int(input('Enter your age: '))
valid_id = input('Do you have a valid id(Yes/no):').lower() 
if valid_id == "yes" :
    valid_id = bool(valid_id)
else :
    valid_id = bool('')


if age >= 18 and valid_id:
    if age >= 60 and valid_id  :
        print('Eligible! and also Eligible for senior discount.')
    else :
        print('Eligible!')

else : 
    print('Not Eligible for discount.')
