gradebook =[
    ['kumar',78,89,93],
    ['pilarmeo',88,99,100],
    ['nagar',89,99,100],
    ['dexter',88,94,91]
    ]
for i in gradebook:
    print(i)

print(gradebook[1][2])
gradebook[2][1] = 100
new_student = ['name',84,91,95]
gradebook.append(new_student)

print(gradebook)