from turtle import *
import random

# define functions
def getRandomColor():
    randomColor = '#' + random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF') + random.choice(
        '0123456789ABCDEF') + random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF') + random.choice(
        '0123456789ABCDEF')
    return randomColor


screen = Screen()
screen.setup(400, 400)
colors = {
    'cheery_red':'#cc263c',
    'parrot_green':'#0dc723',
    'light_blue':'#A2C5F0',
    'dark_pink':'#FA057F'
}
screen.bgcolor(colors['light_blue'])

penup()
speed(0)
for i in range(1, 100):
    x_cod = random.randint(-200, 200)
    y_cod = random.randint(-200, 200)
    goto(x_cod, y_cod)
    dot(100, getRandomColor())
    print(x_cod, " ", y_cod)


goto(0,0)
speed(1)
color('white')
style = ('Arial', 40, 'bold')
write('HELLO', font=style, align='center')
right(90)
forward(60)
color('white')
style = ('Vardana', 30, 'normal')
write('WORLD', font=style, align='center')


speed(5)
goto(-140, 140)
pendown()
forward(280)
left(90)
forward(280)
left(90)
forward(280)
left(90)
forward(280)

penup()
left(90)
goto(-135, 135)
pendown()
forward(270)
left(90)
forward(270)
left(90)
forward(270)
left(90)
forward(270)
left(180)


penup()
goto(-100, -100)
pendown()
forward(200)
speed(1)
penup()
forward(100)





