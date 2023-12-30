import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("catch the turtle")
FONT = ('Arial', 30, 'normal')
#score_turtle

score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = screen.window_height()/2
    y = top_height*0.87
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, font=FONT)

setup_score_turtle()

grid_size = 10
def make_turtle(x, y):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x*grid_size, y*grid_size)
make_turtle(-20, 20)
make_turtle(-10, 20)
make_turtle(0, 20)
make_turtle(10, 20)
make_turtle(20, 20)

make_turtle(-20, 10)
make_turtle(-10, 10)
make_turtle(0, 10)
make_turtle(10, 10)
make_turtle(20, 10)

make_turtle(-20, 0)
make_turtle(-10, 0)
make_turtle(0, 0)
make_turtle(10, 0)
make_turtle(20, 0)

make_turtle(-20, -10)
make_turtle(-10, -10)
make_turtle(0, -10)
make_turtle(10, -10)
make_turtle(20, -10)


turtle.mainloop()