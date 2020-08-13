import turtle
import time
from random import randrange

delay = 0.1

win = turtle.Screen()
win.title("Snake Game by Jezon Fernando")
win.bgcolor("green")
win.setup(width=600, height=600)
win.tracer(0)

# Turtle head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Turtle food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Turtle body
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0 | Highscore: 0", align="center", font=("Consolas", 24, "normal"))

score = 0
highScore = 0


# Directs
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


# Move
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard
win.listen()
win.onkeypress(go_up, "w" or "W")
win.onkeypress(go_down, "s" or "S")
win.onkeypress(go_left, "a" or "A")
win.onkeypress(go_right, "d" or "D")

# Main loop
while True:
    win.update()

    # Death Conditions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for s in segments:
            s.goto(10000, 10000)

        segments.clear()
        score = 0

        delay -= 0.2

        pen.clear()
        pen.write("Score : {} | Highscore: {}".format(score, highScore), align="center", font=("Consolas", 24, "normal"))

    if head.distance(food) < 20:
        # Random Move
        x = randrange(-280, 280, 20)
        y = randrange(-280, 280, 20)
        food.goto(x, y)

        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("grey")
        newSegment.penup()
        segments.append(newSegment)

        delay -= 0.001

        # Score
        score += 10

        # Highscore
        if score > highScore:
            highScore = score

        pen.clear()
        pen.write("Score : {} | Highscore: {}".format(score, highScore), align="center", font=("Consolas", 24, "normal"))

    # Move
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Body Death
    for si in segments:
        if si.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for si in segments:
                si.goto(10000, 10000)

            segments.clear()
            score = 0

            delay -= 0.2
            pen.clear()
            pen.write("Score : {} | Highscore: {}".format(score, highScore), align="center", font=("Consolas", 24, "normal"))
    delay = 0.1
    time.sleep(delay)

win.mainloop()
