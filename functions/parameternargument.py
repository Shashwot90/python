 #Here, n is a parameter of square. A parameter is a variable that is an input to a function.
#It says, “Later, when square is used, you’ll be able to input any value you want, but for now we’ll call that future value n.” 
#A function can have any number of parameters.
#The values of the parameters passed into a function are known as the arguments. Recall in the previous example, we called:
#py square(10)
#Here, the function square was called with the parameter n set to the argument 10.
def power(base,exponent):
    result = base ** exponent
    print('%d to the power of %d is %d' % (base,exponent,result))

power(37,4)    