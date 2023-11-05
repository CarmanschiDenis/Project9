import turtle

#draw = turtle.Turtle()

#for i in range(4):
#    draw.forward(100)
 #   draw.right(90)
#mai complicat
#num_sides = 4
#side_lenght = 40
#angle = 360.0 / num_sides

#for i in range(num_sides):
#    draw.forward(side_lenght)
#    draw.right(angle)
#turtle.done()
#turtle.exitonclick()

#window = turtle.Screen()
#window.bgcolor("white")
#window.title("My Window")

#draw.color("purple")

#def shapefun(size, sides):
 #   for i in range(sides):
  #      draw.fd(size)
   #     draw.right(360.0 / sides)
    #    size = size - 5

#shapefun(150, 4)
#shapefun(130, 4)
#shapefun(110, 4)
#shapefun( 90, 4)
#shapefun(70, 4)
#shapefun(50, 4)
#shapefun(30, 4)
#shapefun(10, 4)

#window2 = turtle.Screen()
#pen = turtle.Pen()
#window2.bgcolor("black")
#colors = ['red', 'yellow', 'blue', 'green','orange', 'purple', 'pink']
#for i in range(360):

 #   turtle.circle(2 * i)
 #   turtle.circle(-2 * i)
 #   turtle.left(i)

  #  pen.pencolor(colors[i%7])
  #  pen.width(i/4666 + 7)
   # pen.forward(i)
 #   pen.left(25)

draw = turtle.Turtle()
draw.speed(2)
draw.pendown()
draw.right(90)
draw.forward(100)
draw.left(45.0)
draw

turtle.done()
turtle.exitonclick()


