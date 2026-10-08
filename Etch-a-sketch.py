from turtle import Turtle , Screen
import turtle

t=Turtle()

def forward():
    t.forward(10)

def backward():
    t.backward(10)

def circlel():
    t.left(180)
    t.circle(50)

def clear():
    turtle.clearscreen()
    turtle.clear()
    
def circler():
    t.right(180)
    t.circle(-50)



s= Screen()
s.listen()
s.onkey(key= 'w' , fun = forward)
s.onkey(key= 's' , fun = backward)
s.onkey(key= 'l' , fun = circlel)
s.onkey(key= 'r' , fun = circler)
s.onkey(key= 'x' , fun = clear)

s.exitonclick()