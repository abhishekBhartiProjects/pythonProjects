#!/bin/python3
from random import randint
from turtle import *

speed(0)
penup()
goto(-140, 140)

for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 100)
ada.pendown()
# for turn in range(100):
#   ada.forward(randint(1,5))

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.pendown()
# for turn in range(100):
#   bob.forward(randint(1,5))

cha = Turtle()
cha.color('green')
cha.shape('turtle')
cha.penup()
cha.goto(-160, 40)
cha.pendown()

aTotal = 0
bTotal = 0
cTotal = 0
aTurned = False
bTurned = False
cTurned = False
for turn in range(200):
    a = randint(1, 5)
    aTotal += a
    ada.forward(a)
    if (aTotal > 300 and not aTurned):
        ada.right(90)
        # ada.forward(5)
        ada.right(90)
        aTurned = True

    b = randint(1, 5)
    bTotal += b
    bob.forward(a)
    if (bTotal > 300 and not bTurned):
        bob.right(90)
        # bob.forward(5)
        bob.right(90)
        bTurned = True

    c = randint(1, 5)
    cTotal += c
    cha.forward(c)
    if (cTotal > 300 and not cTurned):
        cha.right(90)
        # cha.forward(5)
        cha.right(90)
        cTurned = True