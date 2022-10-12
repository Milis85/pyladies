from turtle import left, right, shape, forward, exitonclick, penup, pendown

#prerusovana cara postupne se zvetsujici

for i in range(20):

    pendown()
    forward(5 + i)
    penup()
    forward(2)

exitonclick()