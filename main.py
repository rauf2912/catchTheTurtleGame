import turtle
import random


screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("catch the turtle")
FONT = ('Arial', 30, 'normal')
score = 0
#turtle list
turtle_list = []
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



grid_size = 10
def make_turtle(x, y):
    t = turtle.Turtle()
    def handle_click(x, y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, font=FONT)
       # print(x, y)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x*grid_size, y*grid_size)
    turtle_list.append(t)

x_cordinates = [-20, -10, 0, 10, 20]
y_cordinates = [20, 10, 0, -10]

def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtle_randomly():
    hide_turtles()
    random.choice(turtle_list).showturtle()
    screen.ontimer(show_turtle_randomly, 500)

turtle.tracer(0)

setup_turtles()
setup_score_turtle()
hide_turtles()
show_turtle_randomly()
turtle.tracer(1)


turtle.mainloop()