import turtle


wn = turtle.Screen()
wn.title("Philadelphia Eagles Style Pong") # Changed Title
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A (changed color, position)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("dark green")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-370, 0)

# Paddle B (changed color, position)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("navy blue")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(370, 0)

# Ball (changed shape, color, speed of ball)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .4
ball.dy = .4

# Pen (changed color, scoreboard to say Eagles and Cowboys)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("dark green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Philadelphia Eagles: 0  Dallas Cowboys: 0", align="center", font=("Castellar", 22, "bold"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    # Left and right (Changed scoreboard, took sound out)
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Philadelphia Eagles: {}  Dallas Cowboys: {}".format(score_a, score_b), align="center", font=("Castellar", 22, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Philadelphia Eagles: {}  Dallas Cowboys: {}".format(score_a,score_b), align="center", font=("Castellar", 22, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1


MY VIDEO: https://www.youtube.com/watch?v=huZEUIu2dEc&t=4s

TUTORIAL VIDEO THAT WAS USED: https://www.youtube.com/watch?v=C6jJg9Zan7w

ORIGINAL CODE: http://christianthompson.com/sites/default/files/Pong/pong.py


    
