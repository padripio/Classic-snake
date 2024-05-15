import turtle
import time
from turtle import Screen,Turtle
s=turtle.Screen()

#TODO start of class
class Snake:

    def __init__(self,food_instance):
        turtle_list = []
        self.food_instance=food_instance

        self.turtle_list=turtle_list
    def form_snake(self):

        for i in range(5):
            x=0
            y=0
            t = turtle.Turtle(shape="square")
            t.fillcolor("white")
            t.pencolor("white")
            t.penup()
            t.setx(x)
            t.sety(y)
            x -= 20
            self.turtle_list.append(t)


    # TODO turn left

    def turn_left(self):
        orientation = self.turtle_list[0].heading()
        if orientation == 90:
            self.turtle_list[0].left(90)
        elif orientation == 270:
            self.turtle_list[0].right(90)
        else:None
            #self.turtle_list[0].left(90)


    #TODO turn right

    def turn_right(self):
        orientation = self.turtle_list[0].heading()
        if orientation == 90:
            self.turtle_list[0].right(90)
        elif orientation == 270:
            self.turtle_list[0].left(90)
        else:
            None
            #self.turtle_list[0].right(90)

    #TODO turn up
    def turn_up(self):
        orientation = self.turtle_list[0].heading()
        if orientation == 0:
            self.turtle_list[0].left(90)
        elif orientation == 180:
            self.turtle_list[0].right(90)
        else:
            # illegal
            None


    #TODO turn down
    def turn_down(self):
        orientation = self.turtle_list[0].heading()
        if orientation == 0:
            self.turtle_list[0].right(90)
        elif orientation == 180:
            self.turtle_list[0].left(90)
    # TODO cross y boundaries

    def cross_y(self):

        if self.turtle_list[0].position()[0] > 300:
            x = -300
            y = self.turtle_list[0].position()[1]
            # time.sleep(0.2)
            # turtle.list[0].sety(y)
            for t in self.turtle_list:
                t.setx(x)
                t.sety(y)
                x -= 20
        if self.turtle_list[0].position()[0] < -300:
            x = 300
            y = self.turtle_list[0].position()[1]
            # time.sleep(0.2)
            # turtle.list[0].sety(y)
            for t in self.turtle_list:
                t.setheading(180)
                t.setx(x)
                t.sety(y)
                x += 20

    def cross_walls(self):
        if self.turtle_list[0].position()[1] > 300 or self.turtle_list[0].position()[1] < -300:
            user_input = s.textinput("Game Over ", "  Press 1 to restart ,2 to exit")
            return user_input

   def move_turtles(self):
        length = len(self.turtle_list) - 1

        for turtle_no in range(length, 0, -1):
            x, y = self.turtle_list[turtle_no - 1].position()
            self.turtle_list[turtle_no].goto(x, y)
        self.turtle_list[0].fd(20)


    def extend_snake(self):
        if self.food_instance.collision()==1:
            #find the location of the last turtle
            index=len(self.turtle_list)-1
            xcor,ycor=self.turtle_list[index].position()
            angle=self.turtle_list[index].heading()
            if angle==0:
                xcor-=20
                ycor+=0
            elif angle==180:
                xcor+=20
                ycor+=0
            elif angle==90:
                xcor-=0
                ycor-=20
            elif angle==270:
                xcor-=0
                ycor+=20

            t = turtle.Turtle(shape="square")
            t.fillcolor("white")
            t.pencolor("white")
            t.penup()
            t.setx(xcor)
            t.sety(ycor)
            self.turtle_list.append(t)

 #TODO end of class