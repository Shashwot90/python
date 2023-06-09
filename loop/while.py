from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(input("Your guess: "))
  if guess == random_number:
    print ("You win!")
    break
  guesses_left -= 1
else:
  print ("You lose.")
  
#13
numbers  = [7, 9, 12, 54, 99]

print ("This list contains: ")

for num in numbers:
  print (num)

# Add your loop below!
for number in numbers:
  print (number ** 2)
  
  
#14
 d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:

  # Your code here!
  print (key ,d[key] )
  
#15
choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):
  print (index + 1, item)
  
#16
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  if a > b:
    print (a)
  else:
    print (b)

