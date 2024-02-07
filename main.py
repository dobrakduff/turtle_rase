from turtle import Turtle, Screen
import random
is_rase_t = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="your bet", prompt="input bet")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


y = - 75
for x in range(6):
    names = "turtle" + str(x)
    names = Turtle(shape="turtle")
    names.penup()
    names.color(colors[x])
    names.goto(-230, y)
    y += 30
    all_turtles.append(names)

if user_bet:
    is_rase_t = True

while is_rase_t:
    for turtle in all_turtles:
        if turtle.xcor() < 230:
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print("you won")
            else:
                print(f"you lose win is {win_color}")
        rand = random.randint(0, 10)
        turtle.forward(rand)


screen.exitonclick()