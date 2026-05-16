def passwd_gen(passwd_length):

    import random as rd

#    global passwd_length

 #   while True:
  #      try :
   #         passwd_length = int(input('Enter the password length: '))
    #        break
     #   except: 
      #      continue

    

    while True:
        passwd_length = input('Enter the password length: ')
        for i in len(passwd_length) :
            if passwd_length[i] not in ['1','2','3','4','5','6','7','8','9','0']:
                continue
            


    lower = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = [ i.upper()  for i in lower ]
    numbers = [1,2,3,4,5,6,7,8,9,0]

    passwd = []

    
    

   # passwd = rd.choice(lower)+ rd.choice(upper) + rd.choice(numbers)

    if passwd_length > 1:
        include_upper = input('Include Uppercase (yes/no): ').lower()
        include_lower = input('Include lowercase (yes/no): ').lower()
        include_numbers = input('Include numbers (yes/no): ').lower()
        if include_upper == 'yes' or include_upper =='y':
            if include_lower  == 'yes' or include_lower =='y':
                if include_numbers == 'yes' or include_numbers == 'y' :
                    for i in range(passwd_length) :
                        passwd += rd.choice(lower)+ rd.choice(upper) + str(rd.choice(numbers))
                    
                else : 
                    for i in range(passwd_length) :
                        passwd += rd.choice(upper) + rd.choice(lower)
            else :
                if include_numbers == 'yes' or include_numbers == 'y' :
                    for i in range(passwd_length) :
                        passwd +=  rd.choice(upper) + str(rd.choice(numbers))
                else:
                    for i in range(passwd_length) :
                        passwd +=  rd.choice(upper) 
        else : 
            if include_lower  == 'yes' or include_lower =='y':
                if include_numbers == 'yes' or include_numbers == 'y' :
                    for i in range(passwd_length) :
                        passwd += rd.choice(lower)+ str(rd.choice(numbers))
                    
                else : 
                    for i in range(passwd_length) :
                        passwd += rd.choice(lower) 
            else :
                if include_numbers == 'yes' or include_numbers == 'y' :
                    for i in range(passwd_length) :
                        passwd +=  str(rd.choice(numbers))
                else:
                    print('unable to do without any selection')

        


        final_passwd = rd.choices(passwd,k = passwd_length) 
          
        print('Generated password = ',end = '')
        for i in final_passwd:
            print(i,end='')               
        print(f'\npassword of length {passwd_length}')

    else:
        print('No Passwd with that length!')


 
if __name__ == "__main__":
    while True:
        try :
            passwd_length = int(input('Enter the password length: '))
            break
        except: 
            continue
    
    passwd_gen(passwd_length)
