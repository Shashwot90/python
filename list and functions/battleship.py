from random import randint

board = []#row and column start from 0 till 4 there is no 5 

for x in range(0, 5):
  board.append(["O"] * 5)#adds O to list[o,o,o,o,o] and there are 5 lists inside list

def print_board(board):
  for row in board:
    print( " ".join(row))# join removes the , from list so that o o o o o is printed

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)#random chooses random number from the list. the leangth of board is 5

def random_col(board):
  return randint(0, len(board[0]) - 1)#the length of [o] is also 5

ship_row = random_row(board)#calling function
ship_col = random_col(board)
print (ship_row)# gives the answer of game
print (ship_col)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print ("Turn", turn + 1)#denotes number of turn and turn is increased. goes till 4 
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
#for winning
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!" ) 
    break #if correctly guessed program over
  else:
      #for losing 
    if guess_row not in range(5) or \
      guess_col not in range(5):#if value is 5 or more
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
# if value is repeated only seem after first turn    
    else:#when answer is wrong it stores the value as X
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if turn == 3 :#3 chances provided then game over
      print("Game Over")
    print_board(board)