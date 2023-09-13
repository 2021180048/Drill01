import turtle

def move_by_w():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
def move_by_a():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
def move_by_s():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)
def move_by_d():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)
def restart():
    turtle.reset()
    
turtle.shape("turtle")
turtle.onkey(move_by_w,'w')
turtle.onkey(move_by_a,'a')
turtle.onkey(move_by_s,'s')
turtle.onkey(move_by_d,'d')
turtle.onkey(restart,'Escape')
turtle.listen()

