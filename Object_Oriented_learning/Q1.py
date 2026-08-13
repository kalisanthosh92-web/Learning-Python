class dog:
    ''' A si8mple attemptto madel  a dog. '''

    def __init__(self,name, age):
        self.Name = name
        self.Age = age

    def sit(self):
        print(f'{self.Name} is now sitting.')

    def roll_over(self):
        print(f'{self.Name} rolled over.')



D1 = dog('Lucy', 2)
dog.sit(D1)


print(D1.Name)
      
