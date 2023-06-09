print ('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word:")
if len(original) > 0 and original.isalpha():  # .isalpha() which returns False since the string contains non-letter characters.
  print (original)
else:
  print ("empty")