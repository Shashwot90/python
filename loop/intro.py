count = 0

if count < 10:
  print ("Hello, I am an if statement and count is", count)

while count < 10:
  print ("Hello, I am a while and count is", count)
  count += 1
#2  
num = 1

while num <= 10:  # Fill in the condition
  # Print num squared
  print(num ** 2)
  # Increment num (make sure to do this!)
  num += 1
  
#3
choice = input('Enjoying the course? (y/n)')

while choice != 'y' and choice !='n':  # Fill in the conditio(before the colon)
  choice = input("Sorry, I didn't catch that. Enter again: ")


#5  infinite loop
count = 0

while count < 10: # Add a colon
  
  print (count)
  # Increment count
  count = count + 1# if counter not placed infinite loop
  
#6
count = 0

while True:
  print (count)
  count += 1
  if count >= 10:
    break

#7
import random

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print (num)
  if num == 5:
    print ("Sorry, you lose!")
    break
  count += 1
else:
  print ("You win!")