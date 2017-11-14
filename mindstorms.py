import turtle

def square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(1,37):
        square(brad)
        brad.right(10)

    window.exitonclick()

draw_square()