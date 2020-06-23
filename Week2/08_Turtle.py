import turtle

bob = turtle.Turtle()

# bob.forward(100)  # move 100 pixels
# bob.left(45)
# bob.forward(100)
# bob.right(90)
# bob.forward(100)
# bob.left(45)
# bob.forward(100)

bob.color("blue", "#00FF28")

bob.begin_fill()

bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()


bob.penup()
bob.forward(150)
bob.pendown()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)



turtle.done()  # keeps animation window open
