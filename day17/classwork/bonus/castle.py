import turtle

castle = turtle.Turtle()
castle.color("black")
castle.speed(2)


def draw_rectangle(color, x, y, width, height):
    castle.fillcolor(color)
    castle.penup()
    castle.goto(x, y)
    castle.pendown()
    castle.begin_fill()
    for _ in range(2):
        castle.forward(width)
        castle.left(90)
        castle.forward(height)
        castle.left(90)
    castle.end_fill()


draw_rectangle("gray", -150, -100, 300, 150)


draw_rectangle("lightgray", -150, 50, 50, 100)
draw_rectangle("lightgray", 100, 50, 50, 100)


castle.fillcolor("brown")
castle.penup()
castle.goto(-150, 150)
castle.pendown()
castle.begin_fill()
castle.goto(-125, 200)  
castle.goto(-100, 150)
castle.end_fill()

castle.penup()
castle.goto(100, 150)
castle.pendown()
castle.begin_fill()
castle.goto(125, 200)  
castle.goto(150, 150)
castle.end_fill()


draw_rectangle("blue", -125, 0, 30, 50)
draw_rectangle("blue", 75, 0, 30, 50)

castle.hideturtle()