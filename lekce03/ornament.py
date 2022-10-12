
from turtle import right, left, forward, exitonclick, penup, pendown, pencolor


pocet_stran = 12
uhel = 360 / pocet_stran
strana = 1
pencolor('yellow')
for _ in range(18):
    for i in range(pocet_stran):
        forward(i + strana) 
        left(uhel)
    left(20)
    


exitonclick()


#ctvrecovy ornament
#strana = 1

#for i in range(50):
#    forward(strana + i)
#    left(90)
#
#exitonclick()
