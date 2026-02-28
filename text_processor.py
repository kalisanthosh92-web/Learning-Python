sentence = input('Enter any sentence: ')

print('Sentence in upper case: ',sentence.upper())
print('Sentence in lower case: ',sentence.lower())
print('Sentence in title case: ',sentence.title())

print(sentence.count('a'))
print(sentence.strip())
print(sentence.replace(' ','_'))

list = sentence.strip().split(' ')
for i in sentence.strip().split(' '):
    print(i)

print()
