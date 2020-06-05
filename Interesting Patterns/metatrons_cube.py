import turtle                   # turtle
import time

turtscreen = turtle.Screen()    # window

def circledrawer(L, H):         # L = lower, H = higher
    for i in range(L, H):       # function to move to 
        met.forward(50)         # position and draw circle
        met.right (90)          # then move
        met.circle(50)          # to center
        met.left(90)            # and store position
        met.forward(50)
        circlist[i] = met.pos()

circlist=["X", "X", "X", "X", "X", "X", "X",    ## for storing circle
          "X", "X", "X", "X", "X", "X", "X"]    ## coordinates
 
met = turtle.Turtle()           # turtle is met
dave = turtle.Turtle()          # dave shows platonic solids later
dave.hideturtle()

met.speed(0)                   # turtle speed
dave.speed(0)

met.color("grey")
met.pensize(0.5)
met.penup()
met.goto(0, -50)                # move down a bit
met.setheading(0)
met.pendown()
met.circle(50)                  # draw circle width 50 pixels
met.penup()                     # center at 0,0
met.left(90)
met.forward(50)                 # move to the circles center
circlist[1] = met.pos()         # store the first circles position                                                                   # facing north move 60 degrees east
met.pendown()              
met.goto(circlist[1])           # back to start

circledrawer(2, 4)              # circle drawer does 2 at a time

met.goto(circlist[1])           # then change position
met.setheading(270)             # ready for next 2

circledrawer(4, 6)

met.goto(circlist[1])
met.setheading(90)
met.right(60)

circledrawer(6, 8)

met.goto(circlist[1])
met.setheading(270)
met.right(60)

circledrawer(8, 10)

met.goto(circlist[1])
met.setheading(90)
met.left(60)

circledrawer(10, 12)

met.goto(circlist[1])
met.setheading(90)
met.right(120)

circledrawer(12, 14)

# circles finished... now for lines

met.goto(circlist[11])
met.goto(circlist[3])
met.goto(circlist[7])
met.goto(circlist[13])
met.goto(circlist[5])  ## outer hexagon
met.goto(circlist[9])
met.goto(circlist[11])

met.goto(circlist[2])
met.goto(circlist[6])
met.goto(circlist[12])
met.goto(circlist[4])
met.goto(circlist[8])  ## inner hexagon
met.goto(circlist[10])
met.goto(circlist[2])

met.goto(circlist[7])   ## all the other lines
met.penup()
met.goto(circlist[9])
met.pendown()
met.goto(circlist[13])
met.penup()
met.goto(circlist[11])
met.pendown()
met.goto(circlist[6])
met.penup()
met.goto(circlist[11])
met.pendown()
met.goto(circlist[4])
met.penup()
met.goto(circlist[11])
met.pendown()
met.goto(circlist[5])
met.penup()
met.goto(circlist[11])
met.pendown()
met.goto(circlist[8])
met.penup()
met.goto(circlist[3])
met.pendown()
met.goto(circlist[9])
met.penup()
met.goto(circlist[3])
met.pendown()
met.goto(circlist[8])
met.penup()
met.goto(circlist[3])
met.pendown()
met.goto(circlist[12])
met.penup()
met.goto(circlist[3])
met.pendown()
met.goto(circlist[13])
met.penup()
met.goto(circlist[7])
met.pendown()
met.goto(circlist[10])
met.penup()
met.goto(circlist[7])
met.pendown()
met.goto(circlist[4])
met.penup()
met.goto(circlist[7])
met.pendown()
met.goto(circlist[5])
met.penup()
met.goto(circlist[13])
met.pendown()
met.goto(circlist[2])
met.penup()
met.goto(circlist[13])
met.pendown()
met.goto(circlist[8])
met.penup()
met.goto(circlist[5])
met.pendown()
met.goto(circlist[6])
met.penup()
met.goto(circlist[5])
met.pendown()
met.goto(circlist[10])
met.penup()
met.goto(circlist[9])
met.pendown()
met.goto(circlist[12])
met.penup()
met.goto(circlist[9])
met.pendown()
met.goto(circlist[2])
met.goto(circlist[10])
met.goto(circlist[6])
met.goto(circlist[12])
met.goto(circlist[8])
met.goto(circlist[2])
met.goto(circlist[12])

time.sleep(0.5)

dave.penup()
dave.goto(circlist[11])
dave.pendown()
dave.pensize(5)


dave.color("blue")
dave.goto(circlist[1])
dave.goto(circlist[7])
dave.goto(circlist[3])
dave.goto(circlist[11])
dave.goto(circlist[9])
dave.goto(circlist[5])
dave.goto(circlist[1])
dave.goto(circlist[7])
dave.goto(circlist[13])
dave.goto(circlist[5])
dave.goto(circlist[4])
dave.goto(circlist[12])
dave.goto(circlist[6])
dave.goto(circlist[2])
dave.goto(circlist[10])
dave.goto(circlist[8])
dave.goto(circlist[4])

time.sleep(0.5)

dave.clear()


dave.pensize(5)
dave.color("green")
dave.penup()
dave.goto(circlist[9])
dave.pendown()
dave.goto(circlist[3])
dave.goto(circlist[13])

dave.penup()
dave.goto(circlist[7])
dave.pendown()
dave.goto(circlist[11])
dave.goto(circlist[5])
dave.goto(circlist[7])
dave.penup()
dave.goto(circlist[12])
dave.pendown()
dave.goto(circlist[8])
dave.goto(circlist[2])
dave.goto(circlist[12])
dave.goto(circlist[1])
dave.goto(circlist[9])
dave.goto(circlist[1])
dave.goto(circlist[3])
dave.goto(circlist[1])
dave.goto(circlist[13])
dave.goto(circlist[9])

time.sleep(0.5)

dave.clear()


dave.penup()
dave.goto(circlist[9])
dave.pensize(5)
dave.pencolor("red")
dave.pendown()

dave.goto(circlist[5])
dave.goto(circlist[13])
dave.goto(circlist[9])
dave.goto(circlist[3])
dave.goto(circlist[11])
dave.goto(circlist[9])
dave.goto(circlist[3])
dave.goto(circlist[13])
dave.goto(circlist[7])
dave.goto(circlist[3])

dave.goto(circlist[10])
dave.goto(circlist[8])
dave.goto(circlist[4])
dave.goto(circlist[12])
dave.goto(circlist[6])
dave.goto(circlist[2])
dave.goto(circlist[10])

dave.goto(circlist[8])
dave.goto(circlist[2])
dave.goto(circlist[12])
dave.goto(circlist[8])

time.sleep(0.5)


dave.clear()
dave.penup()

dave.pencolor("purple")
dave.pensize(5)
dave.goto(circlist[8])
dave.pendown()
dave.goto(circlist[2])
dave.goto(circlist[12])
dave.goto(circlist[13])
dave.goto(circlist[7])
dave.goto(circlist[12])
dave.goto(circlist[5])
dave.goto(circlist[13])
dave.goto(circlist[5])
dave.goto(circlist[9])
dave.goto(circlist[11])
dave.goto(circlist[5])
dave.goto(circlist[8])
dave.goto(circlist[9])
dave.goto(circlist[8])
dave.goto(circlist[11])
dave.goto(circlist[3])
dave.goto(circlist[7])
dave.goto(circlist[2])
dave.goto(circlist[11])
dave.goto(circlist[3])
dave.goto(circlist[2])
dave.goto(circlist[8])
dave.goto(circlist[12])


