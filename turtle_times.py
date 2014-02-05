import turtle
import fileinput
import random

wordlist = []

for line in fileinput.input():
  for word in line.strip().split(" "):
    wordlist.append(word)

datalist = [(len(word) if len(word) > 3 else 3, word) for word in wordlist]

window = turtle.Screen()

frank = turtle.Turtle()
frank.speed(10)
count = 0

for pair in datalist:
  window.title(pair[1])
  frank.forward(pair[0]*3)
  turn_angle = random.choice([90,270])  
  frank.left(turn_angle)

turtlescreen = frank.getscreen()
turtlescreen.getcanvas().postscript(file="out.eps")
