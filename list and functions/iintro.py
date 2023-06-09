#1
n = [1, 3, 5]

# Add your code below
print(n[1])

#2
n = [1, 3, 5]
# Do your multiplication here
n[1] = n[1] * 5
print (n)

#3
n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print (n)
#4
number = 5

def my_function(x):
  return x * 3

print (my_function(number))

#5
m = 5
n = 13
# Add add_function here!
def add_function(x,y):
  return x + y


print (add_function(m, n))

#7
n = "Hello"
# Your function here!
def string_function(s):
  return s + ' world'


print (string_function(n))

#9
def list_function(x):
  return x[1]

n = [3, 5, 7]
print (list_function(n))
#10
def list_function(x):
  return x[1]

n = [3, 5, 7]
print (list_function(n))

#11
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
  lst.append(9)
  return lst

print (list_extender(n))

#12
n = [3, 5, 7]
def print_list(x): 
  for i in range(0, len(x)):
    print(x[i],end='\t')

print_list(n)

#13
n = [3, 5, 7]
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
# Don't forget to return your new list!
  return x
print(double_list(n))

#14
def my_function(x):
  for i in range(0, len(x)):
    x[i] #= x[i]
  return x

print (my_function(range(0,3))) # Add your range between the parentheses!

#15
n = [3, 5, 7]

def total(numbers):
  result = 0
  for x in range(0,len(numbers)):
    result += numbers[x]
  return result
print(total(n))

#16
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result=""
  for i in range(0,len(words)):
    result += words[i]
  return result


print (join_strings(n))

#17
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
  return x + y


print (join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]

#18
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for x in numbers:
     results.append(x)
  return results


print (flatten(n))