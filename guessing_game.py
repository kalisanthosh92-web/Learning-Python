number_selected = 45
print('welcome to the guessing game.')

while True:
    num = int(input('Enter a number to guess the number. '))
    if num== number_selected:
        print('Congragulations')
        print(f'the number is {num} and you guessed corectly. ')
        break

