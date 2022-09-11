import turtle
import re


def go():
    turtle.forward(40)
    turtle.right(90)
    turtle.penup()


def choice(n, num):
    if n > 11 or n < 1 or num < 0 or num > 9:
        print("数据错误 n = {}, num={}".format(n, num))
        return

    turtle.penup()
    x = -500 + n*80
    turtle.goto(x, 100)

    if num in [0, 2, 3, 5, 6, 7, 8, 9]:
        turtle.pendown()
    go()
    if num in [0, 1, 2, 3, 4, 7, 8, 9]:
        turtle.pendown()
    go()
    if num in [2, 3, 4, 5, 6, 8, 9]:
        turtle.pendown()
    go()
    if num in [0, 4, 5, 6, 8, 9]:
        turtle.pendown()
    go()

    go()
    turtle.forward(40)

    if num in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        turtle.pendown()
    go()
    if num in [0, 2, 3, 5, 6, 8, 9]:
        turtle.pendown()
    go()
    if num in [0, 2, 6, 8]:
        turtle.pendown()
    go()


turtle.setup(1000, 500)
turtle.pensize(10)

time = "2022年9月11日"

year = time[0:time.rfind('年', 1)]
month = re.findall(r"年(.+?)月", time)
day = re.findall(r"月(.+?)日", time)

i = 1
for y in year:
    choice(i, int(y))
    i += 1
turtle.forward(60)
turtle.write("年", font=("宋体", 50, "normal"))
i += 1

for m in str(month[0]):
    choice(i, int(m))
    i += 1
turtle.forward(60)
turtle.write("月", font=("宋体", 50, "normal"))
i += 1

for d in str(day[0]):
    choice(i, int(d))
    i += 1
turtle.forward(60)
turtle.write("日", font=("宋体", 50, "normal"))
i += 1

turtle.done()
