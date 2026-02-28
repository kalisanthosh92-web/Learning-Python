names = ['Jehan','Alexander','Allen','Plarmeo','nagar']
names2 = ['kumar','kharvi']
for i in names2:
    names.append(i)

for i in names2:
    names.insert(len(names),i)

names[2] = 'santhosh'
names.remove(names[2])

deleted = names.pop()
print(deleted)

print(names)
print(len(names))

