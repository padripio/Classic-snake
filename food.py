import random
from turtle import Screen,  Turtle
import turtle
class Food():

    def __init__(self,snake_instance):
        self.snake_instance=snake_instance
        food = turtle.Turtle(shape="circle")
        food.shapesize(1.3)
        self.food=food
        #super().__init__()

    def Produce(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)

        self.food.fillcolor("white")
        self.food.pencolor("white")
        self.food.penup()
        self.food.goto(x,y)

    #TODO detect collision
    def collision(self):
        flag=0
        #print(f"{self.snake_instance.turtle_list}")
        snake_location=self.snake_instance.turtle_list[0].position()
        food_location=self.food.position()
        difference=[snake_location[0]-food_location[0],snake_location[1]-food_location[1]]
        #print(f"the difference is {difference}")
        if abs(difference[0])<15 and abs(difference[1])<15  :
            self.food.clear()
            flag=1
            return flag

            #food is eaten




