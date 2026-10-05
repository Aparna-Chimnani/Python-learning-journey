from turtle import Turtle, Screen
import random
import turtle

# t= Turtle()
# t.shape('turtle')
turtle.shape('turtle')
turtle.speed('fastest')
turtle.colormode(255)



def random_colour():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)

    value= (r,g,b)
    
    return  value



for i in range(100):

    
    turtle.color(random_colour())
    turtle.circle(100)
   
    current = turtle.heading()
    turtle.setheading(current+10)
    











s= Screen()
s.exitonclick()