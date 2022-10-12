from turtle import fillcolor, begin_fill, forward, left, end_fill, exitonclick

size = 100
color = "#FFE66D"

#nastavi barvu
fillcolor(color)
begin_fill()

#nakresli ctverec
for _ in range(4):
    forward(size)
    left(90)

end_fill()

exitonclick()