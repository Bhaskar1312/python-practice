
letters = ['a', 'b', 'c']
matrix = [[1, 1], [0, 1]]
zeros = [0]*10
print(zeros)

combined = zeros + letters
print(combined)

# [0,1,2,..20] how?
numbers = list(range(21))
print(numbers)

word = list("Hello World!!")
print(word)
print(len(word))
print(word[1:10:2])
print(word[1:])
print(word[::-1])

# list unpacking
first, second, *others, last = word
print(first, second, last, others)

# for loop over lists
for letter in word:
    print(letter, end=',')
print('>>><<<')

# need index of each item
print(enumerate(word))
for index, letter in enumerate(word):
    print(index, letter)

# add/insert/remove items in list
letters = ['a', 'b', 'c']
letters.append('d')
letters.append('d')
print(letters)
letters.insert(0, 'first')
letters.insert(0, 'first')
print(letters)
letters.pop()
print(letters)
letters.pop(2)
print(letters)
letters.remove('first')
print(letters)

del letters[0:3]
print(letters)

letters.clear()
print(letters)

# find objects in a list
letters = ['d','a', 'b', 'c']
print(letters.index('a'))
if 's' in letters:
  print(letters.index('s'))
