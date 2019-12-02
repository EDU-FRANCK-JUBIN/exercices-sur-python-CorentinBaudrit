# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import turtle as tu

Room = [
    {
     "color": "Red",
     "pos" : (0,0),
     "height" : 75 ,
     "width" : 250
     },
     {
     "color": "Blue",
     "pos" : (0,-75),
     "height" : 250 ,
     "width" : 50
     },
     {
     "color": "Grey",
     "pos" : (50,-75),
     "height" : 150 ,
     "width" : 50
     },
     {
     "color": "Orange",
     "pos" : (50,-225),
     "height" : 100 ,
     "width" : 50
     },
     {
     "color": "Green",
     "pos" : (100,-75),
     "height" : 250 ,
     "width" : 150
     }
]

def draw():
    tu.Screen().bgpic("source.gif")
    tu.hideturtle()
    tu.speed(0)
    for i in Room:
        tu.penup()
        tu.goto(i.get("pos"))
        tu.pendown()
        tu.color(i.get("color"))
        tu.begin_fill()
        tu.forward(i.get("width"))
        tu.right(90)
        tu.forward(i.get("height"))
        tu.right(90)
        tu.forward(i.get("width"))
        tu.right(90)
        tu.forward(i.get("height"))
        tu.right(90)
        tu.end_fill()
    tu.done()
    tu.bye()
draw()