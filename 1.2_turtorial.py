'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
merc=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
merc.pensize(3) # width of pen line
merc.speed(10)  # speed of drawing. Go fast to not waste time.
merc.color("#FF4500")
merc.penup()
merc.setpos(70,-120)
merc.pendown()
merc.circle(150,90)
merc.goto(145,35)
merc.circle(70,-90)
merc.goto(70,-120)
merc.penup()
merc.goto(75,220)
merc.pendown()
merc.circle(-150,90)
merc.goto(150,75)
merc.circle(-70,-95)
merc.goto(75,220)
merc.penup()
merc.goto(30,220)
merc.pendown()
merc.circle(-149,-80)
merc.goto(-40,85)
merc.circle(-70,84)
merc.goto(30,220)
merc.penup()
merc.goto(25,-120)
merc.pendown()
merc.circle(133,-102)
merc.goto(-45,35)
merc.circle(65,100)
merc.goto(25,-120)
merc.penup()
merc.setpos(200,-300)
merc.pendown()
merc.pencolor('#FF4500')


merc.write('Ethan Januszewski',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
