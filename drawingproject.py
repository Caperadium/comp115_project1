import turtle
import random

random.seed()

pen = turtle.Turtle()
screen = turtle.Screen()

def draw_leg(): #draws one single brown rectangle
    pen.fillcolor('brown')
    pen.begin_fill()
    pen.right(90)
    for _ in range(2):
        pen.forward(150)
        pen.left(90)
        pen.forward(20)
        pen.left(90)
    pen.end_fill()
    

def draw_tank(length, width): #draws fish tank of certain size
    pen.fillcolor('blue') #draws rectangle of water
    pen.begin_fill()
    for _ in range(2):
        pen.forward(length)
        pen.left(90)
        pen.forward(width)
        pen.left(90)
    pen.end_fill()
    draw_leg() #calls leg draw function to draw leg
    pen.left(90) 
    pen.forward(length-20)
    draw_leg()
    pen.left(90)

def draw_fish(x, y): #draws fish at certain location. It is really not effecient at all but i'm a terrible artist and really wanted to draw a fish
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.fillcolor('black') #draws body
    pen.begin_fill()
    pen.right(45)
    pen.forward(30)
    pen.left(90)
    pen.forward(60)
    pen.right(90)
    pen.forward(15)
    pen.right(45)
    pen.forward(30)
    pen.right(135)
    pen.forward(65)
    pen.left(90)
    pen.forward(40)
    pen.end_fill()

    pen.up()
    pen.fillcolor('white') #draws eyes
    pen.begin_fill()
    pen.left(120)
    pen.forward(13)
    pen.down()
    pen.circle(5)
    pen.end_fill()

def draw_sun(): #calls random function to calculate random number of sun rays, then turtle goes to specified location to draw sun
    num_rays = random.randint(4,16)
    pen.up()
    pen.goto(170,170)
    pen.down()
    pen.fillcolor('yellow')
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()
    angle = 360/num_rays
    pen.up()
    pen.left(90)
    pen.forward(30)

    for i in range(num_rays): #iterates over perviously calculated random number of rays and draws rays
        pen.up()
        pen.forward(30)
        pen.down()
        pen.forward(10)
        pen.up()
        pen.back(40)
        pen.right(angle)

draw_tank(200, 100) #draws tank with legs
draw_fish(20, 50) #draws fish in tank
draw_sun() #draws sun


screen.exitonclick()
