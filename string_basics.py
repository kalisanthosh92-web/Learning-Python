name = input('Enter your full name: ')
n = len(name)
print(f' first character: {name[0]}')
print(f'last character: {name[n-1]}')
#print(name[-1])


print(f'first 5 character: {name[:5]}')
        
print(f'name in reverse: {name[::-1]}')

for i in range(n):
    print(name[i])

if n%2 != 0:
    mid_index = int((n-1) /2)
    print('mid character',name[mid_index])
else:
    mid_index = int((n/2) - 1)
    print('mid character',name[mid_index:mid_index + 2])
    

    
