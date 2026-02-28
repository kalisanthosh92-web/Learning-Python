matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
total = 0
for row in matrix:
    subtotal = 0
    for col in row:
        print(f'{col}',end=' ')
        subtotal += col
        total += col
    print(f'\nsubtotal of {row}st column ={subtotal}')
print(f'\nthe sum of all te elements of the matrix = {total}')


for row in matrix:
    for col in row:
        if row == col:
            print(matrix[row][col],end=' ')

print()


n = 5
for i in range(1,n+1):
    print('*'*i)


        