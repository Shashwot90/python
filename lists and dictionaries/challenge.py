# Prints out the welcome title
print("")
print("Welcome to the Wolving compound interest calculator.\nThis program calculates your potential returns when you invest with us. ")
print("") # leaves a space

# Takes the user information
principle = float(input("Enter starting principle (the amount you start with): "))        #takes the initial investment
rate = float(input("Enter annual interest amount (as a percentage): "))                 #takes the annual interest rate as a percentage
times = int(input("Enter the number of years the amount is invested:  "))               #takes the number years 
number = int(input("Enter the number of times the interest is compounded per year: "))  #takes in the number of times the intest is compounded
print("")

# Calculates compound interest & print out the final interest
annual = principle * (((1 + (rate/(100.0 * number))) ** (number*times)))        # calcukats the interest using the compound interest formula
annual = float(format(annual,'.2f'))                                         # converts the annual to 2.d.p 

# Prints out the final annual investment
print(principle,"invested at",rate,"% for",times,"years compounded",number,"times per year is:",annual)     # prints out the principle,rate,times,number and annual
print("")
print("Here's your individual interest payment and \nThe growth of your balance over time")
print("")

# Header for the table
table = []      #using a list to store data
header =("Year","Period","OldBalance","Interest","NewBalance")      # creates a header for the table 
from tabulate import tabulate    
print(tabulate(table,header,stralign =("center")))                  # tabulate takes a list of lists to create a table

# Initial value
Interest = 0        #set Interest value to 0
counter = 0         #set counter value to 0
year = 0            #set year value to 0

# does the calculation for the investment 
while counter < (times*number):     #creates a loop which take the value of times & number and multiply it together until its equal to the counter 

    Interest = (principle * (rate/(100.0 * number)))        # calculates the total Interest
    Interest = format(Interest,'.2f')                  # converts the Interest to 2.d.p
    OldBalance = principle                                  # setting Oldbalance as the principle
    principle = (principle * (1+(rate/(100.0 * number))))   # calculates the compound interest

    counter = counter + 1       # increment for the counter 

    if counter%4 == 1:          # creates a loop for the year which takes the counter and divide it by 4 to give out the remainder 
        year = year +1          # increment for the year

    table = [["",year,          # creates a list for the table which stores the value of [year,OldBalance,Interest & principle]
              "____",counter,
              "____£",OldBalance,
              "____£",Interest,
              "____£",principle]]
    print(tabulate(table,tablefmt="plain",stralign =("center")))  # prints out loop into a table format

#Displaythetotalsfortheperiod
print ("")
print("Total Interest Earned:£", Interest) # added this so user can see how much interest they have collected #extra