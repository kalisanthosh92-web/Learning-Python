username = 'santhosh.kumar@fcpc.edu.ph'
password = 'Helel_013'

usernm = input('Enter username.')
passwd = input('Enter passwoed.')

if usernm == username:
    if passwd == password :
        print('Welcome, Login succesful!.')
    else:
        print('Incorrect password!')
else :
    print('incorrect username.')
    
