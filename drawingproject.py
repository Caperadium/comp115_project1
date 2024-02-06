import turtle

pen = turtle.Turtle()
screen = turtle.Screen()


def draw_water(length, width): #draws water of certain size
    pen.fillcolor('blue') #draws rectangle of water
    pen.begin_fill()
    for _ in range(2):
        pen.forward(length)
        pen.left(90)
        pen.forward(width)
        pen.left(90)
    pen.end_fill()

def draw_fish(x, y): #draws fish at certain location
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
     
   
    

draw_water(400, 200)
draw_fish(20, 50)

screen.exitonclick()