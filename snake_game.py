import turtle
import time
import random
delay=0.1

# set up the screen
win = turtle.Screen()
win.title("my snake game")
win.bgcolor("green")
win.setup(width=600,height=600)
win.tracer(0)

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("orange")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# Main game loop
while True:
    win.update()

    def move():
        if head.direction == "up":
            y = head.ycor() # y coordinate of the turtle
            head.sety(y + 20)
 
        if head.direction == "down":
            y = head.ycor() # y coordinate of the turtle
            head.sety(y - 20)
 
        if head.direction == "right":
            x = head.xcor() # y coordinate of the turtle
            head.setx(x + 20)
 
        if head.direction == "left":
            x = head.xcor() # y coordinate of the turtle
            head.setx(x - 20)

    def go_up():
        if head.direction != "down":
            head.direction = "up"
 
    def go_down():
        if head.direction != "up":
            head.direction = "down"
 
    def go_right():
        if head.direction != "left":
            head.direction = "right"
 
    def go_left():
        if head.direction != "right":
            head.direction = "left"

    if head.distance(food) < 15:
    # move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
    
  
    # Main game loop
    while True:
        win.update()
        move()
        time.sleep(delay)
    
    # Main game loop
        while True:
            win.update()
            move()
    
    # keyboard bindings
            win.listen()
            win.onkey(go_up, "w")
            win.onkey(go_down, "s")
            win.onkey(go_right, "d")
            win.onkey(go_left, "a")
