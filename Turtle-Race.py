from turtle import Turtle, Screen
import random


s= Screen()
s.setup(width= 500 , height= 400)
race_on= False
user_bet= s.textinput(title= 'Make a bit' , prompt= 'Which color turtle do you think will win?')

print(user_bet)

colors=['red' , 'green' , 'blue' , 'yellow' , 'orange' , 'purple']
yval = [0 , -50 , -100 ,50 , 100]
move = [5 , 10 ,7 ,0]
all_turtles=[]
winner=''
print(winner)

for i in range(0,5):
    tim = Turtle(shape= 'turtle')
   
    tim.color(colors[i])
    tim.penup()
    tim.goto(x= -230 , y= yval[i] )
    all_turtles.append(tim)

if user_bet:
    race_on= True

while(race_on): 
    for turtle in all_turtles:  
       
            turtle.forward(random.choice(move))
    
    if turtle.xcor()>= 230:
                race_on=False  
                winner=turtle.pencolor()

result_turtle = Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(0, 150)

if winner == user_bet:
    result_turtle.write("You guessed right!", align="center", font=("Arial", 24, "normal"))
else:
    result_turtle.write(f"You lose! Winner is {winner}", align="center", font=("Arial", 24, "normal"))




s.exitonclick()