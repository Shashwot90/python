



















#6
animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:10]

#7
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
# Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")

print animals # Observe what prints after the insert operation


#8



my_list = [1,9,3,8,5,7]

for number in my_list:
  # Your code here
  print(2 * number)










#9
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print square_list















#10
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin']) # Prints Puffin's room number

# Your code here!
print (residents['Sloth'])
print( residents['Burmese Python'])






#11
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
menu['Coke'] = 15.50
menu['burger'] = 16
menu['KEN'] = 17
print( menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!




print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)








#12
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Jungle House'


print (zoo_animals)










#13
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
#14
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pocket'] = ['seashell','strange berry','lint']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['backpack'].sort()
# Your code here
inventory['backpack'].remove('dagger')
inventory['gold']= inventory['gold'] + 50