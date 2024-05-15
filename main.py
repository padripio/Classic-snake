# Importing The Turtle Module!.
from turtle import Screen,  Turtle
import turtle
import time
import random
from snake2 import Snake
from food import Food
from scoreboard import Scoreboard
score=Scoreboard()
turtle.listen()
s=turtle.Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
file=open("high.txt")
print(file.read())


#TODO Keep track of score



#TODO adjust snake length
def extend_snake(snake,x):
    if x == 1:
        # find the location of the last turtle
        index = len(snake.turtle_list) - 1
        xcor, ycor = snake.turtle_list[index].position()
        angle = snake.turtle_list[index].heading()
        if angle == 0:
            xcor -= 20
            ycor += 0
        elif angle == 180:
            xcor += 20
            ycor += 0
        elif angle == 90:
            xcor -= 0
            ycor -= 20
        elif angle == 270:
            xcor -= 0
            ycor += 20

        t = turtle.Turtle(shape="square")
        t.fillcolor("white")
        t.pencolor("white")
        t.penup()
        t.setx(xcor)
        t.sety(ycor)
        snake.turtle_list.append(t)


#TODO tail collision

def eat_tail(snake,motion):
    cordinates = []
    count=0
    exits = 0

    if motion >10:
        while True:
            if exits==1:
                break

            for block in snake.turtle_list:
                x,y=block.position()
                list1=[x,y]
                cordinates.append(list1)
            break


        #check for duplicates
        list_of_tuples = [tuple(inner_list) for inner_list in cordinates]
        has_duplicates= len(list_of_tuples)!=len(cordinates)
        if has_duplicates:
            exits=1
        else:
            exits=0

    return exits ,cordinates
def check_tail(snake):

    count=0
    trigger=0
    for x in snake.turtle_list:
        if snake.turtle_list[0].distance(x)<10:

            trigger=1
    #for x in snake.turtle_list:
    #    head_location = snake.turtle_list[0].position()
    #    if count==1:
    #        continue
    #    else:
    #        if snake.turtle_list[0].position()==x.position():
    #            trigger=1
    #            break
    #    count+=1
    return trigger







#TODO SCORE booster
#TODO snipper
#TODO sounds


def main():
    print(file.read())
    list1=[]
    snake=Snake(score)

    food1=Food(snake)


    food1.Produce()

    snake.form_snake()


    turtle.onkey(fun=snake.turn_down, key="Down")
    turtle.onkey(fun=snake.turn_up, key="Up")
    turtle.onkey(fun=snake.turn_left, key="Left")
    turtle.onkey(fun=snake.turn_right, key="Right")


    game_is_on = 1
    s.tracer(0)
    motion=0
    exits=0


    while game_is_on == 1:
        score.write_score()
        #turtle.write(arg=score1,align="left")

        snake.move_turtles()


        exits=check_tail(snake)



        #if exits==1:
            #print(f"game oveeeer")

        if food1.collision() ==1:
            x=1
            extend_snake(snake,x)
            #snake.extend_snake()
            score.update_score()
            food1.Produce()  
        snake.cross_y()
        if snake.cross_walls() == 0:
            game_is_on=0
            break
        elif snake.cross_walls()==1:
            turtle.resetscreen()
            game_is_on=1
            snake.form_snake()

            #None
        time.sleep(0.1)
        s.update()
        motion+=1


if __name__ == "__main__":
    main()

s.exitonclick()

