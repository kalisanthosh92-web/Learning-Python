marks = int(input('Enter marks: '))
if 0 <= marks <= 100:
    if  90<= marks <= 100:
        if marks > 98 :
            print(f'score : {marks} , Grade : A+ ' )
        else :
             print(f'score : {marks} , Grade : A- ' )

    elif 80 <= marks <= 89 :
        if marks > 87 :
            print(f'score : {marks} , Grade : B+ ' )
        else :
             print(f'score : {marks} , Grade : B- ' )

    elif 70 <= marks <= 79 :
        if marks > 77 :
            print(f'score : {marks} , Grade : C+ ' )
        else :
             print(f'score : {marks} , Grade : C- ' )

    elif 60 <= marks <= 69 :
        if marks > 67 :
            print(f'score : {marks} , Grade : D+ ' )
        else :
             print(f'score : {marks} , Grade : D- ' )
    else :
        print(f'score : {marks} , Grade : F ' )

else :
    print('Invald score! ')
