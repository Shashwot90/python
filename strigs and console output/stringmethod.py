#len() counts no of characters
parrot = "Norwegian Blue"
print (len(parrot))

#lower() get rid of all capitalizations in string
parrot = "Norwegian Blue"

print (parrot.lower())

#upper all capitalized
parrot = "norwegian blue"

print (parrot.upper())

#str() convert non-strings to string
"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14

print (str(pi))


#dot notation 
ministry = "The Ministry of Silly Walks"

print (len(ministry))
print (ministry.upper())

#printing strings
"""Tell Python to print "Monty Python"
to the console on line 4!"""
print("Monty Python")

#printing variables
"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print(the_machine_goes)

#string concatenation
# Print the concatenation of "Spam and eggs" on line 3!

print ("Spam "+"and "+"eggs")

#explicit string conversion
# Turn 3.14 into a string on line 3!

print ("The value of pi is around " + str(3.14))

#string formatting with % part 1 % replaces string with %s
string_1 = "Camelot"
string_2 = "place"

print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
# part 2
name = "Alex"
quest = "Teaching Python"
color = "Blue"

print ("Ah, so your name is  %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))

#last
# Write your code below, starting on line 3!

my_string ="hello"
print (len(my_string))
print (my_string.upper())