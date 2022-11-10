import turtle
turtle.bgcolor("Black")
turtle.speed(0)
turtle.hideturtle()
Colors = ["Yellow","Blue","Yellow","red"]

for i in range(100):
    for c in Colors:
        turtle.color(c)
        turtle.circle(180-i, 90)
        turtle.left(90)
        turtle.circle(180-i,90)
        turtle.left(60)

        turtle.end_fill()

turtle.mainloop()
