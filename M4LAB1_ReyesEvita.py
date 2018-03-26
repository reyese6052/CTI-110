# CTI-110
# P4LAB1: Shapes
# Evita L. Reyes
# March 25, 2018
#
import turtle          
win = turtle.Screen()  
t = turtle.Turtle()
y = turtle.Turtle()
# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.color("purple")     # set pencolor (takes string)
t.shape("turtle")
y.pensize(5)
y.color("green")

#commands from here to the last line can be replaced
# triangle, sides are 360 / 3 = 120 degrees
for t in range(3):
    turtle.forward(100)
    turtle.left(120)
for y in range(4):
    turtle.forward(200)
    turtle.right(90)

# end commands
win.mainloop()             # Wait for user to close window
