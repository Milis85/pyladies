from turtle import right, left, forward, penup, pendown, exitonclick
pocet_stran = 95
#vypocet vnejsiho uhlu
uhel = 360 / pocet_stran
#list v pravo
for i in range(20):
    forward(2)
    left(uhel)
left(105)
for i in range(20):
    forward(2)
    left(uhel)
exitonclick()

'''for i in range(18):
    for ctverec in range(4):
        forward(100)
        left(90)
    left(20)

right(90)
forward(200)

exitonclick()'''