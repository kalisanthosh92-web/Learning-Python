#step 1
day  = input('Day (Weekday/Weekend) : ').lower ()
customer = input("Type (Student/Senior/Regular) : ").lower()
time = int(input('showtime hour(9 - 22 ): '))
tickets = int(input('number of tickets.:'))

#step 2
if day == "weekend":
    price = 300.00
else :
    price = 200.00

base_price = price * tickets

if customer == 'student':
    price = base_price * 0.80  #20% off
elif customer == 'senior' :
    price = base_price * 0.70    # 30% off

if time < 12 :
    price = price * 0.90    #10% off 

if tickets > 5:
    price = price *0.95     #0.05% off


# step 3 OUTPUT
print('=== MOVIE TICKET SYSTEM ===')
print(f'Day - {day} \nCustomer - {customer} \nShowtime - {time} \nNumber of tickets = {tickets}\n\n')
print('--RECIEPT--')

print(f'Base price: {base_price} ')

if customer == 'student':
    print(f'Student discount(20%): -{base_price *0.20}')
elif customer == 'senior' :
    print(f'Senior discount(30%): -{base_price *0.30}')

if  time < 12 :
    print(f'matniee discount(10%): -{price * 0.10}')

if tickets > 5 :
    print(f'Group discount(5%): -{price *0.05}')

print('Total:',price )
print('Thank You for the purchase!')
