import turtle
import time
import random
screen=turtle.Screen()
screen.setup(600,630)
screen.bgcolor("black")
screen.tracer(0)
positin_snake=[-20,0,20]
snake_body=[]
starting_pos=[(0,0),(-20,0),(20,0)]

#extend_snake
def extended_part(i):
   mike = turtle.Turtle()
   mike.penup()
   mike.shape("square")
   mike.color("white")
   mike.goto(i)
   snake_body.append(mike)
for i in starting_pos:
   extended_part(i)
def increase_snake():
   extended_part(snake_body[-1].position())

#bubble snake
bubble=turtle.Turtle()
bubble.shape("circle")
bubble.shapesize(stretch_len=0.5,stretch_wid=0.5)
bubble.color("red")
bubble.penup()
x_cor=[]
y_cor=[]
for x in range(-295,295):
   if x%20==0:
       x_cor.append(x)
for y in range(-295,295):
   if y%20==0:
       y_cor.append(y)

#scoreboard
score=0
sum_of_scores=[]
score_pen = turtle.Turtle()
score_pen.color("white")
score_pen.penup()
score_pen.goto(-90, 290)
score_pen.pendown()
score_pen.hideturtle()
score_pen.write(f"current score:{sum(sum_of_scores)}", font=("Calibri", 20, "bold"))
def increase_score():
   score=+1
   sum_of_scores.append(score)

   score_pen.clear()
   score_pen.write("current score:" + str(sum((sum_of_scores))), font=("Calibri", 20, "bold"))

#gameover
def gameover():
   gameover = turtle.Turtle()
   gameover.color("white")
   gameover.penup()
   gameover.goto(-80,0)
   gameover.pendown()
   gameover.hideturtle()
   gameover.write("GAME OVER", font=("Calibri", 20, "bold"))

#real_game_begins
game_on=True
screen.listen()
bubble.goto(random.choice(x_cor), random.choice(y_cor))

while game_on:
   screen.update()
   time.sleep(0.1)
#collision between snake and bubble
   if snake_body[0].distance(bubble) < 15:
       bubble.goto(random.choice(x_cor), random.choice(y_cor))
       score=+1
       increase_snake()
       increase_score()
#snake movements
   for snake in range(len(snake_body)-1,0,-1):
       new_x=snake_body[snake-1].xcor()
       new_y=snake_body[snake-1].ycor()
       snake_body[snake].goto(new_x,new_y)

   snake_body[0].forward(20)

   def move_forward():
       if snake_body[0].heading()==180:
           pass
       else:
           snake_body[0].setheading(0)
           snake_body[0].forward(1)
   def move_rigth():
       if snake_body[0].heading()==270:
           pass
       else:
           snake_body[0].setheading(90)
           snake_body[0].forward(1)
   def move_left():
       if snake_body[0].heading()==90:
           pass
       else:
           snake_body[0].setheading(-90)
           snake_body[0].forward(1)
   def move_back():
       if snake_body[0].heading() == 0:
           pass
       else:
           snake_body[0].setheading(180)
           snake_body[0].forward(1)
   screen.onkey(move_rigth,"Up")
   screen.onkey(move_forward,"Right")
   screen.onkey(move_left,"Down")
   screen.onkey(move_back,"Left")
#wall collision game over
   if snake_body[0].xcor()<-310 or snake_body[0].xcor()>300 or snake_body[0].ycor()>300 or snake_body[0].ycor()<-320:
       gameover()
       game_on=False
#body collision game over
   for segment in snake_body:
       if segment==snake_body[0]:
           pass
       elif snake_body[0].distance(segment)<10:
           gameover()
           game_on=False

screen.exitonclick()

