import turtle
import fileinput
import random

wordlist = []

# Get all words from stdin/specified file name, strip them and add to a list
for line in fileinput.input():
  for word in line.strip().split(" "):
    wordlist.append(word)

# Construct a list of tuples bearing each word and its length except when less than 3 where it is set to 3
datalist = [(len(word) if len(word) > 3 else 3, word) for word in wordlist]

# Initialize the turtle part
window = turtle.Screen()
frank = turtle.Turtle()
frank.speed(10)

for pair in datalist:
  # Update the window title to the word being "interpreted"
  window.title(pair[1])
  
  # Send the turtle forward three times the length of the current word
  frank.forward(pair[0]*3)

  # Make the turtle turn right or left with equal probability
  turn_angle = random.choice([90,270])  
  frank.left(turn_angle)

# Output a copy of the final canvas state as an EPS file
turtlescreen = frank.getscreen()
turtlescreen.getcanvas().postscript(file="out.eps")
