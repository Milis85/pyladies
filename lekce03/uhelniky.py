


from turtle import left, right, forward, exitonclick
pocet_stran = 5
#vypocet vnejsiho uhlu
uhel = 360 / pocet_stran

for i in range(pocet_stran):
    forward(20)
    right(uhel)
left(60)
forward(20)
right(120)
forward(20)

exitonclick()
