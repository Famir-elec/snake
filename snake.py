# PACKAGES:
from tkinter import *
from random import randint
import os
import sys

# Variables:

GAME_WIDTH = 700  # page dimension
GAME_HEIGHT = 700  # page dimension
SPACE_SIZE = 50  # a plate cells
SLOWNESS = 200  # speed game
SNAKE_COLOR = "#12009D"  # snake color
FOOD_COLOR = "#E50606"  # food color
score = 0  # rating
direction = "up"  # direction of movement
BODY_SIZE = 2  # snake size
BACKGROUND_COOLOR = "#22342C"  # background color


# Classes and Functions:
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE  # snake size
        self.cordinates = []  # snake position
        self.square = []  # positon of draw
        # loop to determine position
        for i in range(0, BODY_SIZE):
            self.cordinates.append([0, GAME_HEIGHT])
        # loop to draw position
        for x, y in self.cordinates:
            square = canvas.create_rectangle(x , y , x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tags="snake")
            self.square.append(square)


class Food:
    def __init__(self):
        # position food
        x = randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")


# moving
def next_turn(snake, food):
    x, y = snake.cordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.cordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.square.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text= f"Score: {score}")
        canvas.delete("food")
        food1 = Food()
    else:
        del snake.cordinates[-1]
        canvas.delete(snake.square[-1])
        del snake.square[-1]
    # game over
    if chek_game_over(snake):
        game_over()
    else:
        window.after(SLOWNESS, next_turn, snake, food)


# functions of game over

def chek_game_over(snake):
    x, y = snake.cordinates[0]
    if (x < 0 or x >GAME_WIDTH) :
        return True
    if y < 0 or y >GAME_HEIGHT:
        return True
    for sq in snake.cordinates[1:]:
        if x == sq[0] and y == sq[1]:
            return True
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2, font=("Terminal", 60), text="GAME OVER!",
                       fill="#DF1A2F", tag="gameover")


# function of change direction
def change_direction(new_dir):
    global direction

    if new_dir == "left":
        if direction != "right":
            direction = new_dir
    elif new_dir == "right":
        if direction != "left":
            direction = new_dir
    elif new_dir == "up":
        if direction != "down":
            direction = new_dir
    elif new_dir == "down":
        if direction != "up":
            direction = new_dir


# function of resart
def restart():
    path = sys.executable
    os.execl(path, path, *sys.argv)


# graphic

window = Tk()

window.title("snake :)")  # name window
window.resizable(False,False)# Changing the size of the disabled screen

label = Label(window, text=f"score:{score}", font=("Courier", 30))
label.pack()  # Game Rating
# Canvas Drawing
canvas = Canvas(window, bg=BACKGROUND_COOLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
rstart = Button(window, text="RESTART", fg="red", command=restart)
rstart.pack()
window.update()
# Determining the position of the game
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
