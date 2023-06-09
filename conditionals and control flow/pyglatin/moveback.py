pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print (original)
    word = original.lower()
else:
    print ('empty')
first = word[0]
new_word = word + first + pyg