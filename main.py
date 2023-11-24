from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []
color = ["yellow", "blue", "green", "red", "brown", "purple", "orange"]
turtle_colors = []


class MyTurtle():

    def __init__(self, y):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        screen.colormode(255)
        self.turtle.penup()
        self.turtle.goto(-230, y)

# Set entered color as for user turtle.
    def user_color(self, bet):
        self.turtle.color(bet)
        if bet in color:
            color.remove(bet)

# Method randomly select a color for turtle from the list color.
    def color(self):
        turtle_color = random.choice(color)
        self.turtle.color(turtle_color)
        color.remove(turtle_color)
        return turtle_color

# Method for turtles movement.
    def movement(self):
        move = random.randint(0, 10)
        self.turtle.forward(move)
        if self.turtle.xcor() > 230:
            return True


user_turtle = MyTurtle(-30)
user_color = user_turtle.user_color(bet)
turtle_colors.append(user_color)
all_turtles.append(user_turtle)

# With for ... loop creates 5 turtles from class MyTurtle
for t in range(5):
    new_turtle = MyTurtle(30 * t)
    turtle_color = new_turtle.color()
    turtle_colors.append(turtle_color)
    all_turtles.append(new_turtle)

race_end = False

# With while ... loop turtles will move until one of them achieves finish coordinate.
while race_end == False:
    for index, turtle in enumerate(all_turtles):
        move = turtle.movement()
        if move == True and user_turtle == all_turtles[index]:
            print(f"You're winner. Congratulations!")
            race_end = True
        elif move == True:
            print(f"Winner is {turtle_colors[index]} turtle.")
            race_end = True

screen.exitonclick()
