from turtle import *

screen = Screen()
car = Turtle()
car1 = Turtle()
"""
car.shape("turtle")
car.forward(200)
car.fillcolor("blue")
car.color("red")
car.right(90)
car.forward(200)
car.fillcolor("red")
car.color("green")
car.right(90)
car.forward(200)
car.fillcolor("yellow")
car.color("black")
car.right(90)
car.forward(200)

car1 = Turtle()


car1.fillcolor("red")
car1.begin_fill()
car.fillcolor("blue")
car.color("green")
car1.circle(100)
car1.right(90)
car.fillcolor("red")
car1.color("yellow")
car1.circle(100)
car1.right(90)
car.fillcolor("green")
car1.color("purple")
car1.circle(100)
car1.fillcolor("red")
car1.begin_fill()
car1.right(90)
car.fillcolor("red")
car1.color("red")
car1.circle(100)
car1.end_fill()"""



def makepicture(x,y,r):
    car.pu()
    car.forward(y)
    car.right(x)
    car.circle(r)



for i in range(1,20):
    car.color("black")
    makepicture(10,20,30)



done()




done()