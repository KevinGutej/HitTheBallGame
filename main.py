from tkinter import *
import random
import time
tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)#The windows that has our canvas has to be our first thing we do(top most!).
canvas = Canvas(tk, width=500, height=400, bd=0,highlightthickness=0)#No border around our canvas.
canvas.pack()
tk.update()

class Ball:#Class created called ball.
    def __init__(self,canvas,paddle,kolor):#function init "__" = magic function (change behavor of function).
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill=kolor)#reading function canvas.create.oval and their parameters.
        self.canvas.move(self.id, 245,100)#We are moving the oval to the center of the canvas.
        begin = [-3, -2, -1, 1, 2, 3]
        random.shuffle(begin)
        self.x = begin[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # all happends later in the def funtion.
        position = self.canvas.coords(self.id)  # creating a variable 'position' and calling out the function 'coords' and that function gives us back the cords of x y.Where our oval is in the window.
        if position[1] <= 0:#If position is <= 0 and if the ball hits the top of the screen the ball will stop moving out of our screen
            self.y = 3
        if position[3] >= self.canvas_height: #Checking if position is >= canvas.height (y) up and down.
            self.hit_bottom = True
        if self.hit_paddle(position) == True:
            self.y = -3
        if position[0] <= 0:
            self.x = 3
        if position[2] >= self.canvas_width:#Checking if positon is >= canvas.with (x) left and right.
            self.x = -3

    def hit_paddle(self,pos):#Def of "hit paddle" with the parameters pos.
        paddle_pos = self.canvas.coords(self.paddle.id)#paddle id
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:#first part of if and, checking the position of the racket and the ball position.
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False


class Paddle:#Making out bat
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)#Bat starting point
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)#Setting up the keys so we are able to move our bat left
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)#Setting up the keys so we are able to move our bat right

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):#Allows us to turn left
        self.x = -2
    def turn_right(self, evt):#Allows us to turn right
        self.x = 2

paddle = Paddle(canvas, 'blue')#Calling the function paddle and ball out with their color
ball = Ball(canvas, paddle, 'red')
while 1:#Main loop, contorls most of the program
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)#Speed of the ball