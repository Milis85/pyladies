from turtle import forward, right, left, exitonclick, pencolor, penup, pendown, exitonclick
from math import sqrt


strana = 100
sikcara = strana *sqrt(2)
strecha = sikcara / 2

#dostanu se trochu vlevo a dolu, aby byl obrazek na stredu
left(180)
penup()
forward(250)
left(90)
forward(100)
pendown()
left(90)
pencolor('blue')
#rada domku
for i in range (5):
    for ctverec in range (4):
        forward(strana)
        left(90)
    

    left(45)
    forward(sikcara)
    left(90)
    forward(strecha)
    left(90)
    forward(strecha)
    left(90)
    forward(sikcara)
    left(45)
    forward(30)
# hvezdy, posunu pero trochu nahoru
left(90)
penup()
forward(150)
pendown()
pencolor('yellow')
for h in range(6):
    for i in range(5):
        forward(50)
        right(144)
    
    left(30)
    penup()
    forward(200)
    pendown()


exitonclick()