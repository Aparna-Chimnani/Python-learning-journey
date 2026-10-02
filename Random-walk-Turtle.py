from turtle import Turtle, Screen
import random
import turtle as tim

t = Turtle()
t.shape('turtle')
tim.colormode(255)



# colors = ["red", "blue", "green", "yellow", "purple", "orange", "black"]
angle = [0 , 90 , 180 , 360]


def random_colour():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)

    value= (r,g,b)
    
    return  value


t.speed(5)

for i in range(200):
    t.width(10)
    t.color(random_colour())
    t.setheading(random.choice(angle))
    t.forward(50)
    













s= Screen()
s.exitonclick()