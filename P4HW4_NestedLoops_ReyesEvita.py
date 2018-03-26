# CTI-110
# P4HW4: Nested Loops
# Evita Reyes
# March 25, 2018
#
import turtle
win=turtle.Screen()
t=turtle.Turtle()
t.pensize(10)
turtle.color('yellow')
turtle.Screen().bgcolor('purple')
t.shape('turtle')
t.color('orange')

for t in range(10):
    for t in range(2):
        turtle.forward(200)
        turtle.right(60)
        turtle.forward(200)
        turtle.right(120)
    turtle.right(36)
    
