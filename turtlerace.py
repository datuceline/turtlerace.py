import turtle 
import random

celine = turtle.Turtle()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()


window = turtle.Screen()
window.title("TURTLE RACE")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("TURTLE RACE", font=("Arial", 30, "bold"))
turtle.penup()


turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()


turtle2.speed(0)
turtle2.color("red")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()


turtle3.speed(0)
turtle3.color("blue")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

celine.speed(0)
celine.color("purple")
celine.shape("turtle")
celine.penup()
celine.goto(-250, -50)
celine.pendown()


for i in range(145):
    celine.forward(random.randint(1, 5))
    turtle1.forward(random.randint(1, 5))
    turtle2.forward(random.randint(1, 5))
    turtle3.forward(random.randint(1, 5))
    

turtle.mainloop()
