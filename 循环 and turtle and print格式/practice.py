import turtle as f

f.setup(600, 200)
f.penup()
f.bk(200)
f.pendown()
f.pensize(20)
f.pencolor('red')

length = 5
while length > 0:
    length = length-1
    f.seth(90)
    f.circle(-20, 180)
    f.circle(20, 180)
    f.seth(90)
f.done()