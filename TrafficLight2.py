#This prgram creates functions that draw a traffice light
#By Arturo Ortiz arturo.ortiz1@marist.edu
from graphics import *

def drawTrafficLight(x , y):
    drawLightBody(x , y , 500 , 500)
    drawLamp("green" , 400 , 400 , 50)
    drawLamp("yellow" , 400 , 300 , 50)
    drawLamp("red" , 400 , 200 , 50)
    
def drawLamp(color , x , y , radius):
    lamp = Circle(Point(x , y) , radius)
    lamp.setFill(color)
    lamp.draw(win)
    
def drawLightBody(x , y , length , width):
    body = Rectangle(Point(x , y) , Point(width , length))
    body.setFill("white")
    body.draw(win)
#Draws Traphic light
win = GraphWin("Traffic Light" , 1000 , 1000)    
drawTrafficLight(300 , 100)
