item = input('Enter item name: ')
quantity = input('Enter quantity of the item: ')
unit_price = float(input('Enter unit price: '))
total_price = int(quantity) * unit_price

print(f'{item:<15}')
print(f'{quantity:^5}')
print(f'price: {total_price:,.2f}')

print(f'{'item':<15}|{'quantity':^10}|₱ {'total_price'}')

print(f'{item:<15}|{quantity:^10}|₱ {total_price:,.2f}')

