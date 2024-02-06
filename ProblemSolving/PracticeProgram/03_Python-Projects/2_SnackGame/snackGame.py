import turtle
import random
import time

# scores

score = 0
highsore = 0

# Setup Scrren

wn = turtle.Screen()
wn.title("Snack Game")
wn.bgcolor("#782E2E")
wn.setup(height=700, width=700)

# snack head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#22b14a")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# score board
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("score : 0 & High Score : 0", align="center", font='consolas')


# function
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# moving snack using above functions

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.sety(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.sety(x+20)


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()
    move()
    time.sleep(0.1)
    
    
wn.mainloop()
