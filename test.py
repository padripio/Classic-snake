import random
import turtle
import time
from turtle import Screen,  Turtle
s=turtle.Screen()
snake=turtle.Turtle()
# TODO set screensize
s.screensize(400,400)

snake.shape("square")
#t.goto(465,0)
#t.goto(-465,0)

def look_up():
    possible = 1
    if turtle_list[0].heading()==270:
        possible=0
    if possible==1:
        x,y=turtle_list[0].position()
        for turtle in turtle_list:

            turtle.setheading(90)
            move_snake()
def look_down():
    possible = 1
    if turtle_list[0].heading()==90:
        possible=0
    if possible==1:
        x, y = turtle_list[0].position()
        for turtle in turtle_list:

            turtle.setheading(-90)
            move_snake()


def look_left():
    possible = 1
    if snake.heading()==0:
        possible=0
    if possible==1:
        x, y = turtle_list[0].position()
        for turtle in turtle_list:
            turtle.left(90)
            move_snake()


def look_right():
    possible = 1
    if snake.heading()==180:
        possible=0
    if possible==1:
        x, y = turtle_list[0].position()
        for turtle in turtle_list:
            turtle.right(90)
            move_snake()

#TODO handle events
turtle.listen()
turtle.onkey(look_right,"Right")
turtle.onkey(look_up,key="Up")
turtle.onkey(look_down,key="Down")
turtle.onkey(look_left,key="Left")


# TODO geenerate random food


#move food
food = turtle.Turtle()





food.shape("circle")
def move_food(food):
    food.penup()
    food.pencolor("white")
    food.fillcolor("white")
    x = random.randint(-400, 400)
    y = random.randint(-370, 370)
    food.clear()

    food.goto(x,y)
    food.pencolor("black")
    food.fillcolor("black")
    food.pendown()



def small_move():
    for turtle in turtle_list:
        turtle.penup()
        turtle.fd(10)

def move_snake():
    snake.penup()
    for turtle in turtle_list:
        turtle.penup()
        turtle.fd(2)
    snake.pendown()




#TODO detect food collision

snake.shape("square")
turtle_list=[snake]

def collision():
    while 1:

        snake_pos=turtle_list[0].position()
        food_pos=food.position()
        minus = [snake_pos[0] - food_pos[0], snake_pos[1] - food_pos[1]]
        print(f"field difference is {minus}")
        break

    if abs(minus[0]) < 12  and abs(minus[1]) < 20:
        #time.sleep(1)

        move_food(food)

        #stretching the sanke
        # TODO find shape by adding squares to keep track of head and turning capabilities
        #TODO repair length additom
        turtle_list.append(turtle.Turtle(shape="square"))
        return turtle_list

#TODO form wall boundariesxl
boundary1=[[-400,400],[400,500]]
def check_boundary():
    if (turtle_list[0].position()[1]>395 or turtle_list[0].position()[1]<-395):
        game_over=1
    else:
        game_over=0
    return game_over


over=0
while True:
    while over==0:
        move_snake()
        collision()
        print(f"head is at position {turtle_list[0].position()}")
        print(f"food is at position {food.position()}")
        if check_boundary()==1:
            print("game over")
            over=1
            break
        if over==1:
            break

    print(f"snake location is {snake.position()}")
    break

    #TODO get the field difference
    collision(0.5)



s.exitonclick()