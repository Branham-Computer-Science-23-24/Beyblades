import turtle as trtl

#asigns files to a variable
red = "red.gif"
purple = "purple.gif"
blue = "blue.gif"

#creates screen
wn= trtl.Screen()

#adds the shapes to the screen
wn.addshape(red)
wn.addshape(purple)
wn.addshape(blue)


import turtle as trtl
#This section of the code moves the text "beyblades let it rip" across the screen
# creates turtles
four = trtl.Turtle()
five = trtl.Turtle()
six = trtl.Turtle()

four.hideturtle()
five.hideturtle()
six.hideturtle()
# asigns files to a name
bey = "Beyblades.gif"
let = "let_it.gif"
rip = "rip.gif"

# creates screen
wn= trtl.Screen()

# adds shape to the code
wn.addshape(bey)
wn.addshape(let)
wn.addshape(rip)

# assigns each turtle to the asigned bayblade
four.shape(bey)
five.shape(let)
six.shape(rip)

# lift pen up
four.penup()
five.penup()
six.penup()
#moves the turtles across the screen
four.goto(-400,0)
five.goto(-400,0)
six.goto(-400,0)

four.showturtle()
four.goto(400,0)
four.hideturtle()

five.showturtle()
five.goto(400,0)
five.hideturtle()

six.showturtle()
six.goto(400,0)
six.hideturtle()


import turtle as map

# Gets the turtle in position and helps with setting up the pensize, speed,and color

map.speed(0)
map.pensize(10)
map.penup()
map.right(90)
map.forward(310)
map.left(90)
map.pendown()

# Loop for making both the half circles, one red, one blue. First it sets the
# value of "x". An if else statement to change the pencolor and circle
# position

x = 1
for half_circle in range(2):
    map.pencolor("blue")
    map.circle(310, 180, 75)
    x = 1 + 1
if x == 2:
    map.pencolor("red")
    map.circle(310, 180, 75)
else:
    map.pencolor("blue")
    map.circle(310, 180, 75)

# Initalizes two variables called map_xcor and map_ycor. These are the coordinates used for the map painter to go to.
# This loop draws the two blue lines that criscross. It also reverses the values of map_xcor and map_ycor.


map_xcor = 0
map_ycor = -310

map.pencolor("blue")
for lines in range(2):
    map.goto(map_xcor,map_ycor)
    map.pendown()
    map_xcor = -310
    map_ycor = 0
    map.penup()
    map.goto(310,0)
    map.pendown()
    map.goto(map_xcor,map_ycor)


# Draws the circle in the middle, sets pen thickness and pencolor.
# Also puts coordinates to go to in order to get a perfect circle around the middle

map.pencolor("indigo")
map.fillcolor("indigo")
map.penup()
map.goto(0,30)
map.pensize(4)
map.pendown()
map.begin_fill()
map.circle(30)
map.end_fill()
map.ht()
wn = map.Screen()

# First Beyblade
movement1 = trtl.Turtle()
movement1.penup()
movement1.shape(red)
movement1.goto(200, 0)
movement1.speed(0)
# Second Beyblade
movement2 = trtl.Turtle()
movement2.penup()
movement2.shape(blue)
movement2.goto(-200, 0)
movement2.speed(0)
# Third Beyblade
movement3 = trtl.Turtle()
movement3.penup()
movement3.shape(purple)
movement3.goto(0, 200)
movement3.speed(0)
movement3.right(180)
#sets the condition for the conditional statement
timer = 300

#conditional statement for making the turtles move
while timer > 0:

    movement1.forward(5)
    movement1.left(5)
    movement2.forward(5)
    movement2.left(5)
    movement3.forward(5)
    movement3.left(5)
    timer -= 1

print("Game Over")
wn = trtl.Screen()
wn.mainloop()