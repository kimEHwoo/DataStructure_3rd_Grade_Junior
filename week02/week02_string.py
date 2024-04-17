document = 'Datastr12345uctures'
letters = ''
for c in document:
    if c.isalpha():
        letters += c
print(letters)

words = ['Hello', 'world', 'from', 'Python']
sentence = ' '.join(words)
print(sentence)

lines = ['Line 1', 'Line 2', 'Line 3']
result = '\n'.join(lines)
print(result)

numbers = [1,2,3,4,5]
joined_numbers = ' '.join(map(str, numbers))
print(joined_numbers)