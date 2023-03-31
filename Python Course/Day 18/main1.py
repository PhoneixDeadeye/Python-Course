from turtle import Turtle, Screen
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(199)
# screen = Screen()
# screen.exitonclick()


import turtle as t

tim = t.Turtle()
for _ in range(15):

    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()