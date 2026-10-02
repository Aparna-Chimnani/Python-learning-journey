from turtle import Turtle, Screen
import random

slow= Turtle()
slow.shape('turtle')
slow.color('red')

def shape(side):
    angle = 360 / side
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "black"]

    for i in range(side):
        slow.color(random.choice(colors))
        slow.left(angle)
        slow.forward(100)
        
       
for i in range(3,11):
    shape(i)  
 








screen = Screen()
screen.exitonclick()
