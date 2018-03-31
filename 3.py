# 绘画分形树。
import turtle


def draw_y(size, n):
    for angle in [30, 120]:
        turtle.left(angle)
        if n < 2:
            turtle.pencolor("green")
        else:
            turtle.pencolor("red")
        turtle.fd(size)
        if n != 0:
            draw_y(size / 1.5, n - 1)
            turtle.left(30)
        else:
            turtle.left(180)
        turtle.penup()
        turtle.fd(size)
        turtle.pendown()


turtle.setup(600, 600)
turtle.penup()
turtle.goto(0, -200)
turtle.pensize(1)
turtle.left(90)
turtle.pencolor("red")
turtle.pendown()
level = 5
turtle.fd(150)
draw_y(100, level)
