import turtle


def kline(length, n):
    if n == 1:
        turtle.forward(length)
    else:
        kline(length/3, n-1)
        turtle.left(60)
        kline(length/2, n-1)
        turtle.right(120)
        kline(length/2, n-1)
        turtle.left(60)
        kline(length/3, n-1)


turtle.setup(1600, 800)
turtle.speed(10)
turtle.penup()
turtle.goto(-400, 100)
turtle.pendown()
for i in range(6):
    kline(50, 4)
    turtle.right(60)
turtle.done()
