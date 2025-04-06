# PACKAGES:
import tkinter as tk
from random import randint
import os
import sys

# Variables:

GAME_WITH = 900  # page dimension
GAME_HEIGHT = 900  # page dimension
SPACE_SIZE = 50  # a plate cells
SLOWNESS=100#speed game
SNAKE_COLOR="#12009D"# snake color
FOOD_COLOR="#E50606"#food color
score=0#rating
direction="down"#direction of movement
BODY_SIZE= 2 # snake size
BACKGROUND_COOLOR="#22342C" # background color

#Classes and Functions:
class snake:
    def __init__(self):
        self.body_size=BODY_SIZE# snake size
        self.cordinates=[]# snake position
        self.square=[]#positon of draw
        #loop to determine position
        for i in range(0,BODY_SIZE):
            self.cordinates.append([0,0])
        #loop to draw position
        for x,y in self.cordinates:
            square=tk.cavnvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.square.append(square)


